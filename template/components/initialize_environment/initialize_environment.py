"""
Módulo: initialize_environment
Descrição:
    O fluxograma se inicia no estado de Initialize Environment, seu objetivo é lidar com todo tipo de configuração relacionada ao ambiente de execução do script, limpeza/criação de pastas a serem utilizadas, inicialização de variáveis de globais e tabelas para coleta de informações de relatório.

    Descrição de funções:
        read_config_file: esta função lê o json configurado para receber as variáveis de config e seu output deve ser uma variável global com esses dados para uso em outras etapas do framework

        clear_create_temp_folder: esta função limpa pastas de uso temporário da automação ou cria caso não existam (o ideal é que as pastas usadas sejam todas dentro da estrutura do projeto, nunca pastas de rede nem etc.)

        create_general_variables: esta função é reponsável por criar variáveis globais para uso em outros escopos (tais como variáveis de logs, variáveis de coleta de erro/sucesso e etc) e joga-las na lista de variáveis globais do state machine.

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [02/12/2024]
"""

from template.components.initialize_environment.module.read_config import read_config_file
from utilities.clear_create_temp_folder import clear_create_temp_folder
from template.components.initialize_environment.module.create_general_variables import create_general_variables
from utilities.log_handler import log_info

class InitializeEnvironment:
    def __init__(self, machine):
        self.machine = machine

    def execute(self):
        logger = self.machine.global_variables.get('logger', None)

        log_info(logger, "Initialize Environment", "Inicializando ambiente.")

        read_config_file(self.machine, logger)
        clear_create_temp_folder(self.machine, logger)
        create_general_variables(self.machine, logger)

        log_info(logger, "Initialize Environment", "Inicialização do ambiente completa.")

        from template.components.initialize_applications import InitializeApplications
        self.machine.transition_to(InitializeApplications(self.machine))
