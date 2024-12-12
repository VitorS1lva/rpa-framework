import json
from utilities.log_handler import *

# Função que retorna os aplicativos a serem encerrados citados no JSON de configuração
def get_applications_to_kill(logger):
    """
    Módulo: get_applications_to_kill
    Descrição:
    Este fluxo é responsável por ler o `applications.json` e trazer a lista de aplicativos em execução que devem ser encerrados.
        
    Bibliotecas:
    - `json`: Utilizada para manipulação do arquivo `applications.json`.
    - `utilities.log_handler`: Contém as funções `log_info` e `log_error` para geração de logs.
      - `log_info`: Registra logs de informações gerais.
      - `log_error`: Registra logs relacionados a erros durante a execução.

    Exceções Tratadas:
    - `PermissionError`: Lançada quando o usuário não tem permissão para acessar o arquivo.
    - `FileNotFoundError`: Lançada quando o arquivo `config.json` não é encontrado no caminho especificado.
    - `json.JSONDecodeError`: Lançada quando o arquivo `config.json` não está no formato correto.
    - `Exception`: Captura qualquer outra exceção não prevista durante a execução.
    
    Logs Gerados:
    - Mensagem de sucesso ao carregar a lista de aplicativos.
    - Mensagem de erro detalhada para cada exceção tratada.

    Retorno:
    - Uma lista de aplicativos a serem encerrados.
    """
    try:
        with open('data/applications.json', 'r') as file:
            data = json.load(file)
        log_info(logger, "get_applications_to_kill", "Lista de aplicativos para encerrar carregada com sucesso.")
        return data["ApplicationsToKill"]
    
    except PermissionError as e:
        log_error(logger, "get_applications_to_kill", f"Usuário sem permissão necessária para abrir o arquivo applications.json: {e}")
    
    except FileNotFoundError as e:
        log_error(logger, "get_applications_to_kill", f"O arquivo applications.json não foi encontrado: {e}")
    
    except json.JSONDecodeError as e:
        log_error(logger, "get_applications_to_kill", f"O arquivo applications.json não está no formato correto: {e}")
    
    except Exception as e:
        log_error(logger, "get_applications_to_kill", f"Falha ao carregar aplicativos para serem encerrados: {e}")