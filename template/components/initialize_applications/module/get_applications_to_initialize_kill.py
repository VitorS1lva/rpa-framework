"""
Módulo: initialize_environment
Descrição:
    Este fluxo é responsável por ler o applicatiions.json, e retornar uma lista (para cada função respectivamente) de aplicações que devem ser inicializadas/encerradas.
    
Autor: [vitor.silva@apsen.com.br]
Última Modificação: [04/12/2024]
"""

import json
from utilities.log_handler import log_info, log_error

# Função que retorna os aplicativos a serem inicializados citados no JSON de configuração
def get_applications_to_initialize(logger):
    """Lê a lista de aplicativos a serem inicializados do arquivo de configuração."""
    try:
        with open('config/applications.json', 'r') as file:
            apps = json.load(file)
        log_info(logger, "get_applications_to_initialize", "Lista de aplicativos carregada com sucesso.")
        return apps
    except Exception as e:
        log_error(logger, "get_applications_to_initialize", f"Falha ao carregar a lista de aplicativos a serem inicializados: {e}")
        raise

# Função que retorna os aplicativos a serem encerrados citados no JSON de configuração
def get_applications_to_kill(logger):
    """Lê a lista de aplicativos a serem encerrados do arquivo de configuração."""
    try:
        with open('config/applications.json', 'r') as file:
            config = json.load(file)
        return config.get("ApplicationsToKill", [])
    except Exception as e:
        log_error(logger, "get_applications_to_kill", f"Falha ao carregar aplicativos para serem encerrados: {e}")
        raise
