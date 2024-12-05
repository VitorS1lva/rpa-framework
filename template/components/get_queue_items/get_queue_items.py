"""
Módulo: get_queue_items
Descrição:
    Este estado gerencia a consulta e a validação de itens da fila. Ele busca os itens da base de dados, valida um item de cada vez e o encaminha para o estado `Process` para ser processado.
    - Se não houver mais itens na fila, o estado transita para o `FinalState`.
    - Caso algum item falhe devido a um erro de sistema, o estado transita para o `InitializeEnvironment` antes de retentativas.

Funções:
    - get_queue_items: consulta a base de dados e retorna um item da fila com status "Pendente" para ser processado.
    - validate_queue_items: valida o status e as propriedades dos itens antes de processá-los.

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [03/12/2024]
"""

from utilities.get_queue_items_from_db import get_queue_items_from_db
from utilities.log_handler import log_info, log_error

class GetQueueItems:
    def __init__(self, machine):
        self.machine = machine

    def execute(self):
        # Inicializa variáveis de execução herdadas das variáveis globais
        logger = self.machine.global_variables.get('logger', None)
        max_retries = self.machine.global_variables.get('config', {}).get('max_retries', 3)
        
        log_info(logger, "Get Queue Items", "Buscando um item da fila no Snowflake.")

        try:
            # Buscar apenas um item
            queue_items = get_queue_items_from_db(logger, limit=1)
            
            if not queue_items:
                log_info(logger, "Get Queue Items", "Nenhum item restante na fila. Transitando para o FinalState.")
                from template.components.final_state import FinalState
                self.machine.transition_to(FinalState(self.machine))
            else:
                item = queue_items[0]  # Pegue o único item retornado
                log_info(logger, "Get Queue Items", f"Item {item['ID']} encontrado e enviado para processamento.")

                # Verifica se o item já atingiu o número máximo de tentativas
                retry_count = item.get("retry_count", 0)
                if retry_count >= max_retries:
                    log_info(logger, "Get Queue Items", f"Item {item['ID']} atingiu o limite de {max_retries} tentativas. Atualizando para 'Falha'.")
                    from utilities.update_queue_item_status import update_queue_item_status
                    update_queue_item_status(self.machine, item, "Falha")
                    # Tenta buscar o próximo item após atualizar o status
                    self.execute()
                else:
                    # Adiciona o contador de tentativas ao item
                    item["retry_count"] = retry_count
                    self.machine.queue_items = [item]

                    # Transita para o estado de Process
                    from template.components.process import Process
                    self.machine.transition_to(Process(self.machine))
        except Exception as e:
            log_error(logger, "Get Queue Items", f"Erro ao buscar item da fila: {e}")
            raise