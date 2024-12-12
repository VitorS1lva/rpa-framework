"""
Módulo: log_handler
Descrição:
    Este módulo instância um handler de log para utilizarmos ao longo do framework, bem como diversos níveis de logs a serem registrados.

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [02/12/2024]
"""

import logging
import os
from datetime import datetime

# Diretório padrão para armazenar logs
LOG_DIRECTORY = "logs/"

def get_log_file_name():
    """
    Gera o nome do arquivo de log no formato desejado:
    [DD-MM-YYYY HH:MM:SS] - Log de execução.txt
    """
    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    return f"{timestamp}_Log_de_execucao.txt"

def setup_logger():
    """
    Configura o logger para registrar mensagens em um arquivo e no console.

    :return: Um objeto logger configurado.
    """
    # Certifique-se de que o diretório de logs exista
    if not os.path.exists(LOG_DIRECTORY):
        os.makedirs(LOG_DIRECTORY)

    # Nome do arquivo de log
    log_file_name = get_log_file_name()

    # Configuração do logger
    logger = logging.getLogger("StateMachineLogger")
    logger.setLevel(logging.DEBUG)

    # Formato das mensagens de log
    formatter = logging.Formatter(
        "[ %(asctime)s ] - %(levelname)s - %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S"
    )

    # Handler para registrar no arquivo
    file_handler = logging.FileHandler(os.path.join(LOG_DIRECTORY, log_file_name), encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Handler para registrar no console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Adiciona os handlers ao logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Funções auxiliares para diferentes níveis de log com a inclusão de "Source"
def log_info(logger, source, message):
    """Registra uma mensagem de informação. Usada geralmente em tracking de passos da execução da automação."""
    logger.info(f"{source} - {message}")

def log_warning(logger, source, message):
    """Registra uma mensagem de aviso. Usada geralmente em casos de erro que NÃO comprometem a execução."""
    logger.warning(f"{source} - {message}")

def log_error(logger, source, message):
    """Registra uma mensagem de erro. Usada geralmente em casos de erros que COMPROMETEM a execução."""
    logger.error(f"{source} - {message}")

def log_debug(logger, source, message):
    """Registra uma mensagem de depuração. Usado em casos de debug."""
    logger.debug(f"{source} - {message}")
