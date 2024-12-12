"""
Módulo: read_config_file

Descrição:
Este módulo é responsável por ler o arquivo `config.json` e armazenar os dados lidos 
na variável global `global_variables` do objeto `machine`. Ele garante que as configurações 
sejam inicializadas corretamente para o uso durante o processo.

Bibliotecas:
- `json`: Utilizada para manipulação do arquivo `config.json`.
- `utilities.log_handler`: Contém as funções `log_info` e `log_error` para geração de logs.
  - `log_info`: Registra logs de informações gerais.
  - `log_error`: Registra logs relacionados a erros durante a execução.

Parâmetros:
- `machine` (objeto): Representa o estado atual da máquina. Deve conter o atributo 
  `global_variables` onde as configurações serão armazenadas.
- `logger` (objeto): Instância do logger usada para registrar logs.

Exceções Tratadas:
- `PermissionError`: Lançada quando o usuário não tem permissão para acessar o arquivo.
- `FileNotFoundError`: Lançada quando o arquivo `config.json` não é encontrado no caminho especificado.
- `json.JSONDecodeError`: Lançada quando o arquivo `config.json` não esta no formato correto.
- `Exception`: Captura qualquer outra exceção não prevista durante a execução.

Logs Gerados:
- Mensagem de sucesso ao inicializar o JSON.
- Mensagem de erro detalhada para cada exceção tratada.

Autores:
- [vitor.silva@apsen.com.br]
- [samuel.joseph@apsen.com.br]

Última Modificação:
- 10/12/2024
"""

import json
from utilities.log_handler import *

def read_config_file(machine, logger):
    """
    Lê o arquivo `config.json` e armazena as configurações na variável 
    global `global_variables` do objeto `machine`.

    Parâmetros:
    - machine (objeto): Estado atual da máquina, deve conter o atributo `global_variables`.
    - logger (objeto): Instância do logger para geração de logs.

    Retorno:
    - None

    Exceções Tratadas:
    - `PermissionError`: Loga um erro caso não haja permissão para acessar o arquivo.
    - `FileNotFoundError`: Loga um erro caso o arquivo não seja encontrado.
    - `json.JSONDecodeError`: Lançada quando o arquivo `config.json` não esta no formato correto.
    - `Exception`: Loga erros genéricos e propaga a exceção para depuração.
    """
    try:
        # Abrindo o arquivo config.json para leitura
        with open('data/config.json', 'r') as file:
            # Lendo e armazenando os dados no atributo global_variables
            machine.global_variables['config'] = json.load(file)
        
        # Registrando sucesso na inicialização
        log_info(logger, "read_config_file", "JSON de configuração inicializado com sucesso.")
    
    except PermissionError as e:
        # Registrando erro de permissão
        log_error(logger, "read_config_file", f"Usuário sem permissão necessária para abrir o arquivo config.json: {e}")
    
    except FileNotFoundError as e:
        # Registrando erro de arquivo inexistente
        log_error(logger, "read_config_file", f"O arquivo config.json não foi encontrado: {e}")
    
    except json.JSONDecodeError as e:
        # Registrando erro de formato de arquivo
        log_error(logger, "read_config_file", f"O arquivo config.json não esta no formato correto: {e}")
    
    except Exception as e:
        # Registrando qualquer outro tipo de erro
        log_error(logger, "read_config_file", f"Falha ao ler o JSON de configuração: {e}")
