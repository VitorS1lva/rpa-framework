"""
Módulo: final_state
Descrição:
    O estado FinalState é o responsável por encerrar o processo de automação. 
    Ele limpa recursos, finaliza aplicações e registra informações resumidas sobre o processo.

Funções:
    - cleanup_resources: remove arquivos temporários criados durante a execução.
    - kill_applications: encerra os processos relacionados às aplicações utilizadas.
    - log_summary: registra um resumo final das informações processadas no log.

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [04/12/2024]
"""

from template.components.final_state.module.cleanup_resources import cleanup_resources
from template.components.final_state.module.kill_applications import kill_applications
from template.components.final_state.module.log_summary import log_summary
from utilities.log_handler import log_info, log_error

class FinalState:
    def __init__(self, machine):
        self.machine = machine

    def execute(self):
        logger = self.machine.global_variables.get('logger', None)
        log_info(logger, "Final State", "Iniciando encerramento do processo.")

        try:
            print("Este é o final state...")
            # # Limpa recursos temporários
            # cleanup_resources(logger)

            # # Encerra todas as aplicações relacionadas
            # kill_applications(logger)

            # # Registra um resumo do processo no log
            # log_summary(self.machine, logger)

            # log_info(logger, "Final State", "Processo encerrado com sucesso.")
        except Exception as e:
            log_error(logger, "Final State", f"Erro ao encerrar o processo: {e}")
            raise
