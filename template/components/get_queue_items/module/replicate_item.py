"""

> Este módulo está inutilizado atualmente.


Módulo: initialize_environment
Descrição:
    Este fluxo é responsável por replicar um item na fila localmente para processarmos esse item novamente.
    
Autor: [vitor.silva@apsen.com.br]
Última Modificação: [04/12/2024]
"""

from utilities.log_handler import log_info, log_error

def replicate_item(item, logger):
    """
    Replica um item da fila no final da fila internamente.
    O item é adicionado ao final de uma fila local (não no banco de dados).

    args:
        - item: é o item em questão a ser processado que falhou
        - logger: instância para uso do logger configurado no arquivo main.py
    """
    try:
        log_info(logger, "replicate_item", f"Replicating item with ID {item['ID']} to the end of the local queue.")
        
        # Replicando localmente, adicionando o item no final da fila da máquina.
        # Importante notar que estamos assumindo que self.machine.queue_items é a fila de processamento local.
        # Verifique se a fila de itens da máquina está disponível.
        if hasattr(item['machine'], 'queue_items'):
            item['machine'].queue_items.append(item)
        
        log_info(logger, "replicate_item", f"Item {item['ID']} replicado para o final da fila local.")
    except Exception as e:
        log_error(logger, "replicate_item", f"Failed to replicate item {item['ID']}: {e}")
        raise