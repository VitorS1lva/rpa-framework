"""
Módulo: handle_item_failure
Descrição:
    Gerencia falhas no processamento de itens, replicando-os ou descartando-os
    com base no número de tentativas realizadas.

Funções:
    - handle_item_failure: Decide como tratar um item falhado.

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [03/12/2024]
"""

from template.components.get_queue_items.module.replicate_item import replicate_item

def handle_item_failure(item, logger):
    """
    Gerencia falhas no processamento do item.

    Args:
        item (dict): Dados do item que falhou.
        logger (Logger): Instância do logger para registrar eventos.
    """
    max_retries = 3
    current_retries = item.get("retry_count", 0)

    if current_retries < max_retries:
        item["retry_count"] = current_retries + 1
        replicate_item(item, logger)
        log_info(logger, "Handle Item Failure", f"Item {item['ID']} replicado. Tentativa {item['retry_count']}.")
    else:
        log_info(logger, "Handle Item Failure", f"Item {item['ID']} descartado após {max_retries} tentativas.")
        update_queue_item_status(item['ID'], "Descartado", logger)
