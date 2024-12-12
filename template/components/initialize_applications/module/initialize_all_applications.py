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

Autor: [vitor.silva@apsen.com.br] | [samuel.joseph@apsen.com.br]
Última Modificação: [11/12/2024]
"""
from utilities.log_handler import log_info, log_error
from utilities.Chrome.initialize_chrome import initialize_chrome


def initialize_all_applications(list_of_apps_to_initialize, logger):
    """
    Inicializa todas as aplicações necessárias para o processo.

    Returns:
        list: Lista de dicionários contendo informações sobre as aplicações inicializadas.
    """
    list_of_opened_apps = []
    # TODO: O MODULO `ASSETS` SERA O SNOWFLAKE
    # TODO: CRIAR UM INSTANCIADOR DE APLICATIVOS MAIS ROBUSTO, ONDE ELE PODERA RECEBER EXCEÇÕES
    try:
        log_info(logger, "Initialize All Applications", "Carregando configurações de inicialização das aplicações.")
        # CHAMAR O MODULO DE ABERTURA DE CHROME - SALVAR A INSTANCIA DESSA ABERTURA NA LISTA QUE SERA RETORNADA  (list_of_opened_apps)
        driver = initialize_chrome()
        list_of_opened_apps.append(driver)

        # CHAMAR O MODULO DE ABERTURA DO SAP - SALVAR A INSTANCIA DESSA ABERTURA NA LISTA QUE SERA RETORNADA  (list_of_opened_apps)

        return list_of_opened_apps
    except Exception as e:
        log_error(logger, "Initialize All Applications", f"Erro ao inicializar aplicações: {e}")
        raise
