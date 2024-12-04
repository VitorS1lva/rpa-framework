from template.state_machine import StateMachine
from utilities.log_handler import setup_logger, log_info, log_error

# Função principal do processo
def main():
    # Configuração do logger
    logger = setup_logger()

    try:
        log_info(logger, "Main", "StateMachine execution started.")

        # Inicializa a máquina de estados
        sm = StateMachine()
        sm.global_variables['logger'] = logger  # Passa o logger para a máquina de estados
        sm.run()

        log_info(logger, "Main", "StateMachine execution finished successfully.")

    except Exception as e:
        log_error(logger, "Main", f"An unexpected error occurred: {e}")
        raise  # Relevante para tratar erros críticos no nível superior

if __name__ == "__main__":
    main()
