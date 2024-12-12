"""
Módulo: get_applications_to_initialize_kill
Descrição:
Este fluxo é responsável por ler o `applications.json` e trazer os dados encontrados, os dados serão usados
para matar processos indesejados que estão em execução e para inicializar programas que serão usados ao decorrer do processo. 
    
Bibliotecas:
- `json`: Utilizada para manipulação do arquivo `applications.json`.
- `utilities.log_handler`: Contém as funções `log_info` e `log_error` para geração de logs.
  - `log_info`: Registra logs de informações gerais.
  - `log_error`: Registra logs relacionados a erros durante a execução.

Exceções Tratadas:
- `PermissionError`: Lançada quando o usuário não tem permissão para acessar o arquivo.
- `FileNotFoundError`: Lançada quando o arquivo `config.json` não é encontrado no caminho especificado.
- `json.JSONDecodeError`: Lançada quando o arquivo `config.json` não esta no formato correto.
- `Exception`: Captura qualquer outra exceção não prevista durante a execução.
  
Logs Gerados:
- Mensagem de sucesso ao inicializar o JSON.
- Mensagem de erro detalhada para cada exceção tratada.

Autor: [vitor.silva@apsen.com.br] | [samuel.joseph@apsen.com.br]
Última Modificação: [10/12/2024]
"""

import json
from utilities.log_handler import *

# Função que retorna os aplicativos a serem inicializados citados no JSON de configuração
def get_applications_to_initialize(logger):
    """
    Módulo: get_applications_to_initialize
    Descrição:
    Este fluxo é responsável por ler o `applications.json` e trazer os dados encontrados, os dados serão usados
    para inicializar programas que serão usados ao decorrer do processo. 
        
    Bibliotecas:
    - `json`: Utilizada para manipulação do arquivo `applications.json`.
    - `utilities.log_handler`: Contém as funções `log_info` e `log_error` para geração de logs.
    - `log_info`: Registra logs de informações gerais.
    - `log_error`: Registra logs relacionados a erros durante a execução.

    Exceções Tratadas:
    - `PermissionError`: Lançada quando o usuário não tem permissão para acessar o arquivo.
    - `FileNotFoundError`: Lançada quando o arquivo `config.json` não é encontrado no caminho especificado.
    - `json.JSONDecodeError`: Lançada quando o arquivo `config.json` não esta no formato correto.
    - `Exception`: Captura qualquer outra exceção não prevista durante a execução.
    """

    try:
        with open('data/applications.json', 'r') as file:
            data = json.load(file)
        # log_info(logger, "get_applications_to_initialize", "Lista de aplicativos carregada com sucesso.")
        return data['ApplicationsToInitialize']
    
    except PermissionError as e:
        # Registrando erro de permissão
        log_error(logger, "get_applications_to_initialize", f"Usuário sem permissão necessária para abrir o arquivo applications.json: {e}")

    # except FileNotFoundError as e:
    #     # Registrando erro de arquivo inexistente
        log_error(logger, "get_applications_to_initialize", f"O arquivo applications.json não foi encontrado: {e}")
    
    except json.JSONDecodeError as e:
        # Registrando erro de formato de arquivo
        log_error(logger, "get_applications_to_initialize", f"O arquivo applications.json não esta no formato correto: {e}")

    except Exception as e:
        log_error(logger, "get_applications_to_initialize", f"Falha ao carregar a lista de aplicativos a serem inicializados: {e}")
