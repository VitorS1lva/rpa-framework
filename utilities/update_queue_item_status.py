"""
Módulo: update_queue-item.py
Descrição:
    Este script se encarrega de atualizar o status do item processado no process_item.py no snowflake, seus argumentos de entrada recebem os parâmetros necessário para query e atualização de informações

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [03/12/2024]
"""

from utilities.add_to_report_table import add_to_report_table
from utilities.log_handler import log_error

def update_queue_item_status(machine, item, status, logger, error_type=None, error_message=None):
    """
    Atualiza o status de um item no banco de dados e adiciona informações na tabela de relatórios.

    Args:
        machine (object): Máquina de estados contendo as variáveis globais.
        item (dict): Dicionário com as informações completas do item.
        status (str): Novo status do item (e.g., "Processado", "Erro").
        logger (object): Logger para registrar mensagens.
        error_type (str, optional): Tipo do erro, se aplicável.
        error_message (str, optional): Mensagem de erro detalhada, se aplicável.

    Returns:
        None
    """
    try:
        # Lógica de atualização do status no banco de dados
        from utilities.database_connection import make_database_connection
        conn = make_database_connection()
        cursor = conn.cursor()

        query = f"""
            UPDATE FRAMEWORK.PUBLIC.QUEUE_ITEMS
            SET STATUS = '{status}'
            WHERE ID = '{item.get('ID', None)}'
        """
        cursor.execute(query)
        conn.commit()

        # Atualiza o status no item localmente
        item['Status'] = status

        # Adiciona informações na tabela de relatórios
        add_to_report_table(machine, item, error_type, error_message)
    except Exception as e:
        log_error(logger, "update_queue_item_status", f"Erro ao atualizar status do item {item.get('ID', None)}: {e}")
        raise RuntimeError(f"Erro ao atualizar o status no banco de dados: {e}")
