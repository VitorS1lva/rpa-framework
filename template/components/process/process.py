"""
Módulo: process
Descrição:
    O estado `Process` é responsável por executar o processamento de itens da fila. Para cada item:
    - Realiza o processamento individual utilizando a função `process_item`.
    - Atualiza o status do item no banco de dados Snowflake ao término do processamento.
    - Se ocorrer uma falha, chama `handle_item_failure` para determinar se o item será retentado ou descartado.
    - Transita para o estado `GetQueueItems` para buscar o próximo item, ou `FinalState` caso não haja mais itens.

Descrição de funções:
    - process_item: Implementa a lógica de processamento de um item.
    - handle_item_failure: Gerencia falhas no processamento, decidindo se o item será replicado ou descartado.
    - update_queue_item_status: Atualiza o status do item no banco de dados após o processamento.

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [04/12/2024]
"""

from template.components.process.module.process_item import (
    process_item,
    SUCCESS,
    BUSINESS_RULE_EXCEPTION,
    SYSTEM_EXCEPTION,
)
from utilities.update_queue_item_status import update_queue_item_status
from utilities.log_handler import log_info, log_error

class Process:
    def __init__(self, machine):
        self.machine = machine

    def execute(self):
        config = self.machine.global_variables.get('config', None)
        logger = self.machine.global_variables.get('logger', None)
        current_item = self.machine.queue_items[0] if self.machine.queue_items else None

        if not current_item:
            log_info(logger, "Process", "Nenhum item disponível para processamento. Retornando ao estado GetQueueItems.")
            from template.components.get_queue_items import GetQueueItems
            self.machine.transition_to(GetQueueItems(self.machine))
            return

        log_info(logger, "Process", f"Iniciando processamento do item {current_item['ID']}.")

        try:
            # Processa o item e obtém o status
            status = process_item(current_item, logger, config)

            # Atualiza o status no banco de dados
            update_queue_item_status(current_item['ID'], status, logger)

            if status == SUCCESS:
                log_info(logger, "Process", f"Item {current_item['ID']} processado com sucesso.")
            elif status == BUSINESS_RULE_EXCEPTION:
                log_info(logger, "Process", f"Item {current_item['ID']} descartado por regra de negócio.")
            elif status == SYSTEM_EXCEPTION:
                log_info(logger, "Process", f"Erro de sistema ao processar item {current_item['ID']}. Item será retentado se aplicável.")
        except Exception as e:
            log_error(logger, "Process", f"Erro ao processar item {current_item['ID']}: {e}")
        finally:
            # Remove o item atual da fila e transita para o próximo estado
            self.machine.queue_items.pop(0)
            self.execute()  # Processa o próximo item
