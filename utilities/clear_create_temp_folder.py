import os
import shutil
from utilities.log_handler import log_info, log_error

def clear_or_create_folders(paths, logger):
    """
    Limpa ou cria pastas especificadas na lista de caminhos dentro do JSON de config.
    Apaga todo o conteúdo, incluindo subpastas.
    
    Parâmetros:
        paths (list): Lista de caminhos de pastas a serem limpas/criadas.
        logger: Instância de logger para registro de informações e erros.
    
    Retorna:
        None

    Autor: [vitor.silva@apsen.com.br]
    Última Modificação: [02/12/2024]
    """
    for path in paths:
        try:
            if os.path.exists(path):
                # Apaga todo o conteúdo da pasta e subpastas
                shutil.rmtree(path)
                log_info(logger, "clear_or_create_folders", f"Folder '{path}' cleared.")
            # Cria a pasta novamente
            os.makedirs(path)
            log_info(logger, "clear_or_create_folders", f"Folder '{path}' created.")
        except Exception as e:
            log_error(logger, "clear_or_create_folders", f"Failed to clear/create folder '{path}': {e}")
            raise
