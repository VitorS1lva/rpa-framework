"""
Módulo: Initialize Applications

Descrição:
O módulo **Initialize Applications** é responsável por gerenciar todas as operações relacionadas às aplicações utilizadas durante
o processo de automação. Ele realiza tarefas como inicialização, interrupção e validação das aplicações necessárias.
Este módulo é projetado para ser chamado em momentos específicos do fluxo, mas **não realiza transições automáticas entre estados**.

Funções principais:
1. **`kill_all_applications`**:
   - Encerra todos os processos das aplicações utilizadas na automação.
   - É invocado tanto no estado atual quanto no estado final do fluxo.

2. **`initialize_all_applications`**:
   - Inicializa todas as aplicações essenciais para o processo.
   - Realiza ações como logins e acessos a transações (ex.: SAP).
   - Retorna uma variável que contém as referências às aplicações inicializadas, preparando o ambiente para o estado de `Process`.

3. **`get_applications_to_initialize_kill`**:
   - Lê o arquivo `applications.json` para capturar informações sobre quais aplicações devem ser inicializadas ou encerradas.

4. **`validate_initialized_applications`**:
   - Valida se as instâncias das aplicações inicializadas estão ativas e prontas para uso no processo.

Detalhes importantes:
- Este módulo garante a preparação e o encerramento adequado do ambiente de aplicações.
- As configurações e variáveis utilizadas são extraídas de arquivos de configuração, como `applications.json`.

Autor: [vitor.silva@apsen.com.br] | [samuel.joseph@apsen.com.br]

Última Modificação:
- 10/12/2024
"""

from utilities.log_handler import *
from template.components.initialize_applications.module.kill_all_applications import kill_all_applications
from template.components.initialize_applications.module.initialize_all_applications import initialize_all_applications
from template.components.initialize_applications.module.get_applications_to_kill import get_applications_to_kill
from template.components.initialize_applications.module.get_applications_to_initialize import get_applications_to_initialize

class InitializeApplications:
    """
    Módulo: Initialize Applications

    Descrição:
    O módulo **Initialize Applications** é responsável por gerenciar todas as operações relacionadas às aplicações utilizadas durante
    o processo de automação. Ele realiza tarefas como inicialização, interrupção e validação das aplicações necessárias.
    Este módulo é projetado para ser chamado em momentos específicos do fluxo, mas **não realiza transições automáticas entre estados**.

    Funções principais:
    1. **`kill_all_applications`**:
    - Encerra todos os processos das aplicações utilizadas na automação.
    - É invocado tanto no estado atual quanto no estado final do fluxo.

    2. **`initialize_all_applications`**:
    - Inicializa todas as aplicações essenciais para o processo.
    - Realiza ações como logins e acessos a transações (ex.: SAP).
    - Retorna uma variável que contém as referências às aplicações inicializadas, preparando o ambiente para o estado de `Process`.

    3. **`get_applications_to_initialize_kill`**:
    - Lê o arquivo `applications.json` para capturar informações sobre quais aplicações devem ser inicializadas ou encerradas.

    4. **`validate_initialized_applications`**:
    - Valida se as instâncias das aplicações inicializadas estão ativas e prontas para uso no processo.

    DETALHES IMPORTANTES:
    - Este módulo garante a preparação e o encerramento adequado do ambiente de aplicações.
    - As configurações e variáveis utilizadas são extraídas de arquivos de configuração, como `applications.json`.
    """

    def __init__(self, machine, logger):
        self.machine = machine
        self.logger = logger

    def execute(self):
        # logger = self.machine.global_variables.get('logger', None)
        log_info(self.logger, "Initialize Applications", "Inicializando aplicações...")

        try:
            # Ler informações sobre as aplicações
            applications_to_kill = get_applications_to_kill(self.logger)

            # Matar instâncias anteriores das aplicações
            kill_all_applications(applications_to_kill, self.logger)

            # TODO: EXCLUIR ESTE MODULO JA QUE AS APLICAÇÕES VÃO VIR DIRETAMENTE DO config.json -- FALAR COM O BRUNO ANTES PARA VER SE FOI ENCONTRADA
            # UMA SOLUÇÃO PARA ARMAZENAMENTO DE ASSETS
            applications_to_initialize = get_applications_to_initialize(self.logger)

            # Inicializar novas instâncias das aplicações
            initialized_apps = initialize_all_applications(applications_to_initialize, self.logger)

            self.machine.global_variables['initialized_apps'] = initialized_apps 

            log_info(self.logger, "Initialize Applications", "Aplicações inicializadas com sucesso.")
        except Exception as e:
            log_error(self.logger, "Initialize Applications", f"Erro ao inicializar aplicações: {e}")
            raise