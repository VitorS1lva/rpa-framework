"""
Módulo: initialize_environment
Descrição:
    Este fluxo é responsável por inicializar as variáveis globais do processo, bem como data table de coleta de informação de itens processados.
    
Autor: [vitor.silva@apsen.com.br]
Última Modificação: [04/12/2024]
"""

from utilities.log_handler import log_info

def create_general_variables(machine, logger):
    """
    Inicializa variáveis globais no framework.

    - Para acessar o config dentro do state desejado pode-se usar a seguinte sintaxe ("config = self.machine.global_variables.get('config', None)")
    """
    machine.global_variables = {
        'logger': None,  # Placeholder para logger
        'config': None,  # Placeholder para config.json
        'error_table': [
            {'ID': None, 'ErrorType': None, 'ErrorMessage': None}  # Modelo inicial com colunas declaradas
        ]
    }
    log_info(logger, "create_general_variables", "Variáveis globais inicializadas com sucesso.")
