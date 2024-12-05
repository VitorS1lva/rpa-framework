"""
Função: cleanup_resources
Descrição:
    Limpa os arquivos temporários criados durante a execução do processo.

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [04/12/2024]
"""

import shutil
import os

def cleanup_resources(logger):
    temp_folder = "./temp"
    if os.path.exists(temp_folder):
        shutil.rmtree(temp_folder)
        logger.info("Recursos temporários limpos com sucesso.")
    else:
        logger.info("Nenhuma pasta temporária encontrada para limpar.")
