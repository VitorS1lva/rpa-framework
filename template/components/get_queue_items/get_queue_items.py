"""
Módulo: get_queue_items

Descrição:
Este módulo gerencia os itens de fila, faz a requisição dos itens no banco de dados e atualiza o status dos itens com base no resultado da execução.
- Se não houver itens na fila, o estado transita para o `FinalState`.
- Caso algum item falhe devido a um erro de sistema ou atinja o número máximo de tentativas, o status do item é atualizado para "Falha" e outro item
é processado.

Funções principais:
    - __init__: Inicializa o estado atual da máquina de estados.
    - execute: Realiza as seguintes etapas:
        1. Busca itens pendentes no banco de dados.
        2. Gera logs para cada ação realizada.
        3. Atualiza o status do item para "Falha" caso o número máximo de tentativas seja atingido.
        4. Transita para o estado `FinalState` se não houver itens na fila.
        5. Transita para o estado `Process` para processar o item de fila atual.

Exceções:
    - Lança uma exceção caso ocorra um erro inesperado durante o processamento de itens da fila.

Autor: [vitor.silva@apsen.com.br] | [samuel.joseph@apsen.com.br]
Última Modificação: [10/12/2024]
"""

from utilities.update_queue_item_status import update_queue_item_status
from utilities.get_queue_items_from_db import get_queue_items_from_db
from template.components.final_state import final_state
from template.components.process.process import process
from utilities.log_handler import *

class GetQueueItems:
    """
    Classe responsável por gerenciar o estado de obtenção de itens de fila.

    Métodos:
        - __init__: Inicializa a classe com a máquina de estados fornecida.
        - execute: Busca itens na fila e os processa conforme as regras definidas.
    """

    def __init__(self, machine):
        """
        Inicializa a classe com a máquina de estados fornecida.

        Args:
            machine (StateMachine): Instância atual da máquina de estados.
        """
        self.machine = machine

    def execute(self, logger):
        """
        Busca itens na fila no banco de dados e gerencia o fluxo de transição de estados.

        Etapas:
            1. Busca itens pendentes no banco de dados.
            2. Gera logs para cada ação realizada.
            3. Atualiza o status do item para "Falha" caso o número máximo de tentativas seja atingido.
            4. Transita para o estado `FinalState` se não houver itens na fila.
            5. Transita para o estado `Process` para processar o item de fila atual.

        Exceções:
            - Lança uma exceção caso ocorra um erro durante a busca ou processamento dos itens da fila.
        """

        max_retries = self.machine.global_variables.get('config', {}).get('max_retries', 3)        

        try:        
            while True:
                # Buscar apenas um item da fila
                #queue_items = get_queue_items_from_db(logger)
                queue_items = {
                    "id": 1,
                    "creation_date_time": "",
                    "job_id": "",
                    "specificContent": {
                        "nomeDoVideo": "Aula de C# 1 - Iniciante"
                    }
                }
                
                log_info(logger, "Get Queue Items", "Buscando item da fila no banco de dados.")

                if not queue_items:
                    log_info(logger, "Get Queue Items", "Nenhum item restante na fila. Transitando para o FinalState.")
                    self.machine.transition_to(final_state(self.machine))
                    break


                while True:
                    item = queue_items[0]  # Pega o único item retornado
                    log_info(logger, "Get Queue Items", f"Item {item['ID']} encontrado e enviado para processamento.")

                    # Transita para o estado de Process
                    status, error_message = process(item, logger)

                    if status == "SUCCESS":
                        log_info(logger, "Process", f"Item {item['ID']} processado com sucesso.")
                        update_queue_item_status(item, "Sucesso", logger, error_message)
                    elif status == "BUSINESS_RULE_EXCEPTION":
                        log_info(logger, "Process", f"Item {item['ID']} descartado por regra de negócio.")
                        update_queue_item_status(item, "BRE", logger, error_message)
                    elif status == "SYSTEM_EXCEPTION":
                        item["retry_number"] += 1 
                        if item["retry_number"] >= max_retries:   
                            log_info(logger, "Get Queue Items", f"Item {item['ID']} atingiu o limite de {max_retries} tentativas. Atualizando para 'Falha'.")
                            update_queue_item_status(item, "Falha", logger, error_message)
                            break
                        log_info(logger, "Process", f"Erro de sistema ao processar item {item['ID']}. Item será retentado pela {item["retry_number"]} vez.")
        
        except Exception as e:
            log_error(logger, "Get Queue Items", f"Erro ao buscar item da fila: {e}")