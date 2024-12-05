"""
Módulo: initialize_applications
Descrição:
    O estado de Initialize Applications tem como objetivo tratar quaisquer assuntos relacionados às aplicações utilizadas no script.
    Ele é projetado para ser invocado em momentos específicos do processo, mas **não realiza transições automáticas no fluxo**.

    Descrição de funções:
        kill_all_applications: esta função encerra todos os processos das aplicações que serão utilizadas na automação (invocado neste estado e no final state).

        initialize_all_applications: esta função inicializa todas as aplicações necessárias para o processo, retornando uma variável que aponta para as aplicações.
        Nesta etapa, também pode-se considerar logins e acessos a transações (ex.: SAP). Seu objetivo é preparar o ambiente para o estado de Process.

        get_applications_to_initialize_kill: esta função lê o arquivo `applications.json` e captura as variáveis com informações de interrupção e inicialização das aplicações a serem manipuladas.

        validate_initialized_applications: esta função valida as instâncias inicializadas das aplicações que serão utilizadas no processo.

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [04/12/2024]
"""

from utilities.log_handler import log_info, log_error
from template.components.initialize_applications.module.kill_all_applications import kill_all_applications
from template.components.initialize_applications.module.initialize_all_applications import initialize_all_applications
from template.components.initialize_applications.module.get_applications_to_initialize_kill import get_applications_to_initialize
from template.components.initialize_applications.module.get_applications_to_initialize_kill import get_applications_to_kill
from template.components.initialize_applications.module.validate_initialized_applications import validate_initialized_applications

class InitializeApplications:
    def __init__(self, machine):
        self.machine = machine

    def execute(self):
        logger = self.machine.global_variables.get('logger', None)
        log_info(logger, "Initialize Applications", "Inicializando aplicações...")

        try:
            # Ler informações sobre as aplicações
            applications_to_kill = get_applications_to_kill(logger)

            # Matar instâncias anteriores das aplicações
            kill_all_applications(applications_to_kill, logger)

            # Inicializar novas instâncias das aplicações
            initialized_apps = initialize_all_applications()

            # Validar inicializações
            validate_initialized_applications(initialized_apps, logger)

            log_info(logger, "Initialize Applications", "Aplicações inicializadas com sucesso.")
        except Exception as e:
            log_error(logger, "Initialize Applications", f"Erro ao inicializar aplicações: {e}")
            raise
