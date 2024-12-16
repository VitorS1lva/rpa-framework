from utilities.log_handler import *
from template.components.initialize_applications.module.kill_all_applications import kill_all_applications
from template.components.initialize_applications.module.get_applications_to_kill import get_applications_to_kill

def initialize_applications(config, logger):
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

   Autor(es):
   - [vitor.silva@apsen.com.br]
   - [samuel.joseph@apsen.com.br]

   Última Modificação:
   - 16/12/2024
   """
   # logger = self.machine.global_variables.get('logger', None)
   log_info(logger, "Initialize Applications", "Inicializando aplicações...")

   # TODO: O MODULO `ASSETS` SERA O SNOWFLAKE
   # TODO: CRIAR UM INSTANCIADOR DE APLICATIVOS MAIS ROBUSTO, ONDE ELE PODERA RECEBER EXCEÇÕES
   # TODO: ACESSAR A VARIÁVEL list_of_opened_apps EM ESCOPO GLOBAL E DAR APPEND DOS ITENS A ELA

   try:
      # Ler informações sobre as aplicações
      applications_to_kill = get_applications_to_kill(logger)

      # Matar instâncias anteriores das aplicações
      kill_all_applications(applications_to_kill, logger)

      # Abaixo deste comentário entra a lógica do desenvolvedor para incialização de aplicações,
      # estas lógicas devem retornar uma variável com a instância da aplicação inicializada, se possível.
      # Essas instâncias serão adicionadas a uma variável de escopo global, para serem utilizadas em outros estados externos.
      
      log_info(logger, "Initialize Applications", "Aplicações inicializadas com sucesso.")
      
   except Exception as e:
      log_error(logger, "Initialize Applications", f"Erro ao inicializar aplicações: {e}")
      raise