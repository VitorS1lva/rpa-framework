"""
Função: log_summary
Descrição:
    Registra um resumo final das informações processadas no log.

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [04/12/2024]
"""

def log_summary(machine, logger):
    total_items = machine.global_variables.get("total_items_processed", 0)
    success_items = machine.global_variables.get("success_items", 0)
    failed_items = machine.global_variables.get("failed_items", 0)

    logger.info(f"Resumo Final: Total: {total_items}, Sucesso: {success_items}, Falha: {failed_items}")
