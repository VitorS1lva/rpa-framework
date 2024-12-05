"""
Módulo: initialize_all_applications
Descrição:
    Este módulo é responsável por inicializar todas as aplicações necessárias para o processo. 
    Ele pode incluir logins, acessos a transações e qualquer outra configuração essencial para o funcionamento correto das aplicações.

    A função principal retorna uma lista de objetos ou variáveis que representam as instâncias das aplicações inicializadas.

Funções:
    - initialize_all_applications: inicializa as aplicações necessárias com base nas configurações fornecidas.
        - Lê as configurações do arquivo `applications.json`.
        - Inicia os processos das aplicações.
        - Retorna uma lista contendo as instâncias inicializadas.

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [04/12/2024]
"""

import json
import subprocess
from utilities.log_handler import log_info, log_error
from pathlib import Path

def initialize_all_applications():
    """
    Inicializa todas as aplicações necessárias para o processo.

    Returns:
        list: Lista de dicionários contendo informações sobre as aplicações inicializadas.
    """
    initialized_apps = []
    logger = None  # Substituir pelo logger global se disponível.

    try:
        log_info(logger, "Initialize All Applications", "Carregando configurações de inicialização das aplicações.")
        
        # Carregar configurações do arquivo applications.json
        config_path = Path("config/applications.json")
        if not config_path.exists():
            log_error(logger, "Initialize All Applications", "Arquivo application.json não encontrado.")
            raise
        
        with open(config_path, 'r') as config_file:
            applications_config = json.load(config_file)

        for app_config in applications_config.get("applications", []):
            app_name = app_config.get("name")
            executable = app_config.get("executable_path")
            arguments = app_config.get("arguments", [])

            log_info(logger, "Initialize All Applications", f"Iniciando a aplicação: {app_name}")
            
            if not executable or not Path(executable).exists():
                log_error(logger, "Initialize All Applications", f"Caminho do executável inválido para a aplicação: {app_name}")
                continue

            # Comando para iniciar o processo da aplicação
            command = [executable] + arguments
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            initialized_apps.append({
                "name": app_name,
                "process": process
            })
            
            log_info(logger, "Initialize All Applications", f"Aplicação {app_name} inicializada com sucesso.")
        
        return initialized_apps

    except Exception as e:
        log_error(logger, "Initialize All Applications", f"Erro ao inicializar aplicações: {e}")
        raise
