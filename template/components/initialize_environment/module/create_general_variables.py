from utilities.log_handler import log_info

def create_general_variables(machine, logger):
    """Inicializa variáveis globais adicionais."""
    machine.global_variables['log'] = []
    log_info(logger, "create_general_variables", "Variáveis globais inicializadas com sucesso.")
