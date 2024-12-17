"""
Módulo: Initialize Environment

Descrição:
Este módulo tem como objetivo preparar o ambiente de execução do script. Ele realiza configurações essenciais,
como a limpeza e criação de pastas necessárias, inicialização de variáveis globais e criação de tabelas para coleta
de informações destinadas a relatórios. Este é o primeiro passo para garantir que o framework funcione de forma consistente e organizada.

Funções principais:
1. **`read_config_file`**:
   - Lê o arquivo JSON de configuração (config.json).
   - Armazena os dados encontrados em uma variável global para que possam ser usados em outras etapas do framework.

2. **`clear_create_temp_folder`**:
   - Limpa pastas temporárias utilizadas pela automação ou as cria caso não existam.
   - Recomendação: As pastas utilizadas devem estar dentro da estrutura do projeto e nunca em locais de rede ou externos.

3. **`create_general_variables`**:
   - Inicializa variáveis globais necessárias para diferentes escopos.
   - Exemplos de variáveis criadas: variáveis para logs, coleta de erros/sucessos, e outras informações de execução.
   - Adiciona essas variáveis à lista global do state machine.

Autor(es):
- [vitor.silva@apsen.com.br]
- [samuel.joseph@apsen.com.br]

Última Modificação:
- 10/12/2024
"""

from template.components.initialize_environment.module.read_config_file import read_config_file
from template.components.get_queue_items.get_queue_items import GetQueueItems
from utilities.clear_create_temp_folder import clear_create_temp_folder
from template.components.initialize_environment.module.create_general_variables import create_general_variables
from utilities.log_handler import log_info
from template.components.initialize_applications.initialize_applications import *


class InitializeEnvironment:
    """
    Este módulo tem como objetivo preparar o ambiente de execução do script. Ele realiza configurações essenciais,
    como a limpeza e criação de pastas necessárias, inicialização de variáveis globais e criação de tabelas para coleta
    de informações destinadas a relatórios. Este é o primeiro passo para garantir que o framework funcione de forma consistente e organizada.

    Funções principais:
    1. **`read_config_file`**:
    - Lê o arquivo JSON de configuração (config.json).
    - Armazena os dados encontrados em uma variável global para que possam ser usados em outras etapas do framework.

    2. **`clear_create_temp_folder`**:
    - Limpa pastas temporárias utilizadas pela automação ou as cria caso não existam.
    - Recomendação: As pastas utilizadas devem estar dentro da estrutura do projeto e nunca em locais de rede ou externos.

    3. **`create_general_variables`**:
    - Inicializa variáveis globais necessárias para diferentes escopos.
    - Exemplos de variáveis criadas: variáveis para logs, coleta de erros/sucessos, e outras informações de execução.
    - Adiciona essas variáveis à lista global do state machine.

    """

    def __init__(self, machine):
        self.machine = machine
        
    def execute(self):
        
        self.logger = self.machine.global_variables.get('logger', None)
        log_info(self.logger, "Initialize Environment", "Inicializando ambiente.")

        # Cria as variáveis globais
        create_general_variables(self.machine, self.logger)

        # Lê o arquivo de configuração
        read_config_file(self.machine, self.logger)
        
        # Limpa ou cria as pastas temporárias
        clear_create_temp_folder(self.machine, self.logger)
        
        log_info(self.logger, "Initialize Environment", "Inicialização do ambiente completa.")

        try:
            # TODO: Adicionar lógica de retrieve de JOB Id
            
            # Transição para o estado InitializeApplications - Proximo modulo
            #log_info(self.logger, "Initialize Environment", "Executando InitializeApplications para preparar o ambiente.")
            # intialize_applications(self.logger)


            # O Desenvolvedor deve chamar a func start applications


            # Transição para o estado GetQueueItems - Proximo modulo
            log_info(self.logger, "GetQueueItems ", "Executando GetQueueItems para pegar os itens de fila.")
            self.machine.transition_to(GetQueueItems(self.machine))
            init_applications = GetQueueItems(self.machine)
            init_applications.execute(self.logger)

        except Exception as e:
            log_info(self.logger, "Initialize Environment", f"Erro ao executar InitializeApplications: {e}")

