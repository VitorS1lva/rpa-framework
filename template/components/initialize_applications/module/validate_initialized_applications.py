from utilities.log_handler import log_info, log_error

def validate_initialized_applications(initialized_apps, logger):
    """
    Valida se os aplicativos foram inicializados corretamente.

    Args:
        initialized_apps (dict): Dicionário com os aplicativos e seus processos iniciados.
        logger: Instância do logger.
    """
    for app_name, process in initialized_apps.items():
        if process.poll() is not None:  # Verifica se o processo ainda está ativo
            log_error(logger, "validate_initialized_applications", f"{app_name} falhou ao permanecer ativo.")
        else:
            log_info(logger, "validate_initialized_applications", f"{app_name} ativo e operante.")
