"""
Módulo: initialize_applications
Descrição:
    Com o sucesso do  estado de Initialize Environment a etapa de Initialize Applications tem como objetivo tratar quaisquer assuntos relacionados às aplicações utilizadas no script.

    Descrição de funções:
        kill_all_applications: esta função mata todos os processos de aplicações que serão utilizadas na automação (invocado neste estado e no final state)

        initialize_all_applications: esta função inicializa quaisquer aplicações utilizadas no processo, retornando uma variável que aponte para a aplicação, nesta etapa também deve-se considerar fazer logins, acesso a transações (SAP por exemplo), sua função é deixar o terreno o mais preparado possível para o estado de process

        get_applications_to_initialize_kill: esta função é responsável por ler o arquivo applications.json(data) e dentro do arquivo capturar as variáveis que contém informações de interrupção e incialização de arquivos que se deseja manipular

        validate_initialized_applications.py: esta função é responsável por validar as instâncias inicializadas das aplicações que serão utilizadas no processo

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [02/12/2024]
"""

from template.components.initialize_applications.module.get_applications_to_initialize_kill import get_applications_to_initialize
from template.components.initialize_applications.module.get_applications_to_initialize_kill import get_applications_to_kill
from template.components.initialize_applications.module.kill_all_applications import kill_all_applications
from template.components.initialize_applications.module.initialize_all_applications import initialize_all_applications
from template.components.initialize_applications.module.validate_initialized_applications import validate_initialized_applications
from utilities.log_handler import log_info

class InitializeApplications:
    def __init__(self, machine):
        self.machine = machine
        self.initialized_apps = {}

    def execute(self):
        logger = self.machine.global_variables.get('logger', None)

        log_info(logger, "Initialize Applications", "Inicializando aplicações.")

        # Executa as funções do estado
        apps_to_initialize = get_applications_to_initialize(logger)
        apps_to_kill = get_applications_to_kill(logger)
        kill_all_applications(apps_to_kill, logger)
        self.initialized_apps = initialize_all_applications(apps_to_initialize, logger)
        validate_initialized_applications(self.initialized_apps, logger)

        log_info(logger, "Initialize Applications", "Aplicações inicializadas com sucewsso.")

        # Passa para o próximo estado com os aplicativos inicializados
        self.machine.global_variables['initialized_apps'] = self.initialized_apps
        from template.components.get_queue_items import GetQueueItems
        self.machine.transition_to(GetQueueItems(self.machine))
