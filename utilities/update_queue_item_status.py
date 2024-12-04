"""
Módulo: update_queue-item.py
Descrição:
    Este script se encarrega de atualizar o status do item processado no process_item.py no snowflake, seus argumentos de entrada recebem os parâmetros necessário para query e atualização de informações

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [03/12/2024]
"""

from utilities.log_handler import log_info, log_error
from utilities.database_connection import make_database_connection

def update_queue_item_status(item_id, status, logger):
    """
    Atualiza o status de um item específico na tabela QUEUE_ITEMS no banco de dados Snowflake.

    Args:
        item_id (str): ID do item a ser atualizado.
        status (str): Novo status do item.
        logger: Logger para registrar eventos.

    Raises:
        Exception: Se ocorrer um erro ao atualizar o status no banco.
    """
    try:
        # Registrar início da atualização
        log_info(logger, "update_queue_item_status", f"Atualizando status do item {item_id} para {status}.")

        # Conectar ao banco de dados
        connection = make_database_connection()
        cursor = connection.cursor()

        # Query para atualizar o status
        query = """
            UPDATE FRAMEWORK.PUBLIC.QUEUE_ITEMS
            SET STATUS = %s, UPDATED_AT = CURRENT_TIMESTAMP
            WHERE ID = %s
        """
        # Executar a query com parâmetros
        cursor.execute(query, (status, item_id))

        # Confirma a transação
        connection.commit()

        # Registrar sucesso
        log_info(logger, "update_queue_item_status", f"Status do item {item_id} atualizado com sucesso para {status}.")

    except Exception as e:
        # Registrar erro e relançar a exceção
        log_error(logger, "update_queue_item_status", f"Erro ao atualizar status do item {item_id}: {e}")
        raise
    finally:
        # Fechar conexão e cursor, garantindo liberação de recursos
        try:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        except Exception as close_error:
            log_error(logger, "update_queue_item_status", f"Erro ao fechar conexão ou cursor: {close_error}")
