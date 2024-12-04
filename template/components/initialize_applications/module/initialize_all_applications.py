from template.components.initialize_applications.module.get_applications_to_initialize_kill import get_applications_to_kill
from template.components.initialize_applications.module.get_applications_to_initialize_kill import get_applications_to_initialize
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

        log_info(logger, "Initialize Applications", "Inicializando aplicações")

        # Obtém a lista de aplicativos para terminar do arquivo de configuração
        apps_to_kill = get_applications_to_kill(logger)
        if apps_to_kill:
            kill_all_applications(apps_to_kill, logger)

        # Executa as outras funções do estado
        apps_to_initialize = get_applications_to_initialize(logger)
        self.initialized_apps = initialize_all_applications(apps_to_initialize, logger)
        validate_initialized_applications(self.initialized_apps, logger)

        log_info(logger, "InitializeApplications", "Aplicações inciailizadas com sucesso.")

        # Passa para o próximo estado com os aplicativos inicializados
        self.machine.global_variables['initialized_apps'] = self.initialized_apps
        from template.components.get_queue_items import GetQueueItems
        self.machine.transition_to(GetQueueItems(self.machine))
