import os
from utilities.log_handler import log_info, log_error

def kill_all_applications(applications_to_kill, logger):
    """
    Finaliza todos os processos relacionados aos aplicativos especificados.

    Args:
        applications_to_kill (list): Lista de nomes de aplicativos a serem finalizados (ex.: ['app1.exe', 'app2.exe']).
        logger: Instância do logger.
    """
    try:
        if not applications_to_kill:
            log_info(logger, "kill_all_applications", "Sem aplicações específicadas para serem encerradas.")
            return

        for app in applications_to_kill:
            os.system(f'taskkill /IM {app} /F')  # Força a finalização do processo pelo nome
            log_info(logger, "kill_all_applications", f"Aplicação encerrada com sucesso: {app}")

    except Exception as e:
        log_error(logger, "kill_all_applications", f"Falha ao encerrar aplicação: {e}")
        raise