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

Autor: [vitor.silva@apsen.com.br] | [samuel.joseph@apsen.com.br]
Última Modificação: [11/12/2024]
"""

from utilities.treat_errors import BRE, SE
from utilities.log_handler import log_info, log_error
from template.components.process.app.Chrome.initialize_chrome import initialize_chrome
from template.components.process.app.Chrome.Youtube.search_for_videos import search_for_videos


# TODO: PASSAR AS INSTANCIAS DE PROGRAMAS ABERTOS
def process(item, logger):
    log_info(logger, "Process", f"Iniciando processamento do item {item}.")

    try:
        status = "SUCESSO"
        error_message = ""
        
        #Passo a passo do processo entra abaixo deste comentário
        driver = initialize_chrome() # startar chrome
        status , error_message = search_for_videos(driver) # script
        
        return status, error_message
    except Exception as e:
        log_error(logger, "Process", f"Erro ao processar item {item['id']}: {e}")
        status = "SYSTEM EXCEPTION"
        error_message = e
        return status, error_message