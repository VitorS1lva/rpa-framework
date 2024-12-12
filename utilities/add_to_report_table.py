"""
Módulo: update_queue-item.py
Descrição:
    Este script se encarrega de alimentar a tabela de coleta de status globais do process, sua função é carregar as informações de processamento de itens para o final state, onde poderemos consolidar em um excel e enviar via e-mail aos usuários.
    
Autor: [vitor.silva@apsen.com.br]
Última Modificação: [04/12/2024]
"""

def add_to_report_table(item, status, logger, error_message):
    """
    Adiciona informações sobre um item processado na tabela global de relatórios.

    Importante lembrar que as colunas específicadas aqui devem ser as mesmas que foram declaradas junto da incialização da tabela no create_general_variables.py

    Args:
        machine (object): Máquina de estados contendo as variáveis globais.
        item (dict): Dicionário com as informações completas do item.
        error_type (str, optional): Tipo do erro (e.g., "Business Exception", "System Exception").
        error_message (str, optional): Mensagem detalhada sobre o erro.

    Returns:
        None
    """
    try:
        # Obtém a tabela de relatórios
        report_table = machine.global_variables.get('error_table', [])

        # Adiciona o item ao relatório, incluindo tipo e mensagem de erro, se aplicáveis
        report_table.append({
            'nomeDoVideo': item.get('nomeDoVideo', None),
            'errortype': status,
            'errormessage': error_message
        })

        # Atualiza a variável global
        machine.global_variables['error_table'] = report_table
    except Exception as e:
        raise RuntimeError(f"Erro ao adicionar item na tabela de relatórios: {e}")
