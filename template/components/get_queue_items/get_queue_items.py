"""
Módulo: get_queue_items
Descrição:
    Este estado gerencia a consulta e a validação de itens da fila. Ele busca os itens da base de dados, valida um item de cada vez e o encaminha para o estado `Process` para ser processado.
    - Se não houver mais itens na fila, o estado transita para o `FinalState`.
    - Caso algum item falhe durante o processamento, a função `replicate_item` é chamada para movê-lo ao final da fila de itens.

Funções:
    - get_queue_items: consulta a base de dados e retorna um item da fila com status "Pendente" para ser processado.
    - replicate_item: replica um item falhado, adicionando-o ao final da fila de itens.
    - validate_queue_items: valida o status e as propriedades dos itens antes de processá-los.

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [03/12/2024]
"""

from utilities.get_queue_items_from_db import get_queue_items_from_db
from template.components.get_queue_items.module.replicate_item import replicate_item
from utilities.log_handler import log_info, log_error

class GetQueueItems:
    def __init__(self, machine):
        self.machine = machine

    def execute(self):
        logger = self.machine.global_variables.get('logger', None)

        log_info(logger, "Get Queue Items", "Consolidando queue items da base de dados.")

        try:
            queue_items = get_queue_items_from_db(logger)
            if not queue_items:
                log_info(logger, "Get Queue Items", "Sem queue items encontrados, seguindo para o Final State.")
                from template.components.final_state import FinalState
                self.machine.transition_to(FinalState(self.machine))
            else:
                for item in queue_items:
                    # Valida o item antes de processá-lo
                    if item.get("status") == "Pendente":
                        log_info(logger, "Get Queue Items", f"Item {item['ID']} pronto para processamento.")
                        self.machine.queue_items = [item]  # Transfere apenas um item por vez para o próximo estado
                        from template.components.process import Process
                        self.machine.transition_to(Process(self.machine))
                        return  # Finaliza o processamento após passar um item de cada vez

                    # Se o item falhar e precisar ser retentado
                    if 'retry_item' in item and item['retry_item']:
                        replicate_item(item, logger)
                        log_info(logger, "Get Queue Items", f"Item {item['ID']} replicado no final da fila.")
                        
                        # Transita para processar o próximo item após a replicação
                        self.execute()

        except Exception as e:
            log_error(logger, "Get Queue Items", f"Erro ao consolidar queue items: {e}")
            raise