import snowflake.connector

def make_database_connection():
    """
    Cria e retorna uma conexão com o banco de dados Snowflake.

    Retorna:
        snowflake.connector.connection.SnowflakeConnection: Um objeto de conexão ao banco de dados Snowflake.

    Levanta:
        snowflake.connector.errors.Error: Se ocorrer um erro genérico relacionado à conexão com o banco de dados.
        snowflake.connector.errors.DatabaseError: Se ocorrer um erro específico relacionado ao banco de dados.
        Exception: Para quaisquer outros erros inesperados.

    Observações:
        - O usuário, senha, conta, banco de dados e esquema estão atualmente configurados de forma fixa 
          (deveriam ser obtidos de forma mais segura, como de um gerenciador de credenciais ou arquivo de configuração).
        - O parâmetro `quote_identifiers` está ativado para assegurar que identificadores sejam citados corretamente.

    Autor: [Samuel Pierre] - EMAIL [samuel.joseph@apsen.com.br]
    Última Modificação: [02/12/2024] - Vitor Silva
    """
    try:
        conn = snowflake.connector.connect(
            user='rpaorch',
            password='Rpa2024@',
            account='nra45017.east-us-2.azure',
            database='FRAMEWORK',
            schema='PUBLIC',
            quote_identifiers=True
        )
        return conn
    except snowflake.connector.errors.Error as e:
        raise snowflake.connector.errors.Error(f"Erro ao conectar ao banco de dados: {e}")
    except snowflake.connector.errors.DatabaseError as e:
        raise snowflake.connector.errors.DatabaseError(f"Erro ao conectar ao banco de dados: {e}")
    except Exception as e:
        raise Exception(f"Erro inesperado: {e}")
