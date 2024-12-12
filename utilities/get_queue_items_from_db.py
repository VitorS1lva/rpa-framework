"""
Módulo: get_queue_items_from_db
Descrição:
    Este módulo fornece uma função para ler a tabela de queue_items
    localizado no banco de dados FRAMEWORK. É usado para carregar todos os queue items que não tem JOB_ID atribuido.

Funções:
    - get_queue_items_from_db(): Lê a tabela queue_items no banco de dados e trás os itens
    que fila que não possuem JOB_ID atribuido.
    
Exceções:
    ConnectionError: Erro generico de conexão
    ConnectionRefusedError: Erro de conexão recusada
    Exception: Erros não mapeados nas exceções
Usos (Opcional):
    - É possivel alterar os dados que virão do banco de dados

Autor: [Samuel Pierre] - EMAIL [samuel.joseph@apsen.com.br]
Última Modificação: [04/12/2024] - Vitor Silva
"""

from utilities.database_connection import make_database_connection
from utilities.log_handler import log_error

def get_queue_items_from_db(logger, limit):
    """
    Consulta o banco de dados Snowflake e retorna os itens da fila com status "Pendente".
    
    Parâmetros:
        logger (Logger): Instância do logger para registrar erros.

    Retorna:
        list: Lista de itens da fila com status "Pendente".

    Levanta:
        Exception: Para quaisquer erros durante a consulta e manipulação do banco de dados.
    """
    # TODO: RETORNAR APENAS 1 ITEM
    try:
        conn = make_database_connection()
        cursor = conn.cursor()
        query = """
            SELECT * 
            FROM QUEUE_ITEMS 
            WHERE job_id IS NULL 
                AND FOLDERS_ID = '{process_id}'
                AND STATUS = 'Pending';
        """
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        log_error(logger, "get_queue_items_from_db", f"Failed to retrieve queue items: {e}")
        raise
