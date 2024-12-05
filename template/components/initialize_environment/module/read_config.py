"""
Módulo: initialize_environment
Descrição:
    Este fluxo é responsável por ler o config.json
    
Autor: [vitor.silva@apsen.com.br]
Última Modificação: [04/12/2024]
"""

import json
from utilities.log_handler import log_info, log_error

def read_config_file(machine, logger):
    """Lê o arquivo de configuração e salva em variáveis globais."""
    try:
        with open('config/config.json', 'r') as file:
            machine.global_variables['config'] = json.load(file)
        log_info(logger, "read_config_file", "JSON de configuração inicializado com sucesso.")
    except Exception as e:
        log_error(logger, "read_config_file", f"Falha ao ler o JSON de configuração: {e}")
        raise
