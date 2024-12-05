"""
Função: kill_applications
Descrição:
    Encerra os processos relacionados às aplicações utilizadas no processo.

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [04/12/2024]
"""

import psutil

def kill_applications(logger):
    applications = ["application1.exe", "application2.exe"]  # Substituir pelos nomes reais
    for app in applications:
        for process in psutil.process_iter(attrs=["pid", "name"]):
            if process.info["name"] == app:
                process.terminate()
                logger.info(f"Aplicação {app} encerrada com sucesso.")
