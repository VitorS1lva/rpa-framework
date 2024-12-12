"""
Módulo: create_general_variables
Descrição:
Este fluxo é responsável por inicializar as variáveis globais do processo `machine.global_variables`, bem como
a data table de coleta de informação de itens processados.

Bibliotecas:
- `utilities.log_handler`: Contém as funções `log_info` e `log_error` para geração de logs.
  - `log_info`: Registra logs de informações gerais.
  - `log_error`: Registra logs relacionados a erros durante a execução.

Parâmetros:
- `machine` (objeto): Representa o estado atual da máquina. Deve conter o atributo 
  `global_variables` onde as configurações serão armazenadas.
- `logger` (objeto): Instância do logger usada para registrar logs.

Exceções Tratadas:
- None

Autor: [vitor.silva@apsen.com.br] | [samuel.joseph@apsen.com.br]
Última Modificação: [10/12/2024]
"""

from utilities.log_handler import log_info

def create_general_variables(machine, logger):
    """
    Este fluxo é responsável por inicializar as variáveis globais do processo `machine.global_variables`, bem como
    a data table de coleta de informação de itens processados.

    Parâmetros:
    - `machine` (objeto): Representa o estado atual da máquina. Deve conter o atributo 
    `global_variables` onde as configurações serão armazenadas.
    - `logger` (objeto): Instância do logger usada para registrar logs.
    """
    machine.global_variables = {
        'logger': None,  # Placeholder para logger
        'config': None,  # Placeholder para config.json
        'error_table': [
            {'ID': None, 'ErrorType': None, 'ErrorMessage': None}  # Modelo inicial com colunas declaradas
        ]
    }
    log_info(logger, "create_general_variables", "Variáveis globais inicializadas com sucesso.")
