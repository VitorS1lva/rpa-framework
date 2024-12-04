"""
Módulo: process_item
Descrição:
    Contém a lógica principal para processar um item da fila.
    Este módulo deve incluir e ser adaptado de acordo com as regras de negócio específicas.
    A pasta APP na árvore do projeto é destinada a guardar lógicas de criação do processo, como boa prática fica definido que nenhum código deve ser marretado aqui, o espaço deste script é apenas para chamar funções.

Funções:
    - process_item: Processa o item e registra logs apropriados.

Autor: [vitor.silva@apsen.com.br]
Última Modificação: [03/12/2024]
"""

from utilities.log_handler import log_info, log_error

# Definição de constantes para os status
SUCCESS = "success"
BUSINESS_RULE_EXCEPTION = "business_rule_exception"
SYSTEM_EXCEPTION = "system_exception"

def process_item(item, logger):
    """
    Processa um item e retorna o status do processamento.

    Args:
        item (dict): O item da fila.
        logger: Logger para registrar eventos.

    Returns:
        str: O status do processamento (SUCCESS, BUSINESS_RULE_EXCEPTION, SYSTEM_EXCEPTION).
    """
    try:
        # Simulação da lógica de processamento
        log_info(logger, "process_item", f"Processing item ID {item['ID']}.")
        
        # Exemplo de lógica de sucesso
        if item.get('type') == 'valid':
            return SUCCESS
        # Exemplo de lógica de exceção de regra de negócio
        elif item.get('type') == 'business_error':
            return BUSINESS_RULE_EXCEPTION
        # Simulação de uma exceção
        else:
            raise ValueError("System error occurred.")
    except Exception as e:
        log_error(logger, "process_item", f"System exception while processing item ID {item['ID']}: {e}")
        return SYSTEM_EXCEPTION
