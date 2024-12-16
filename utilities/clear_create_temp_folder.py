"""
Módulo: clear_create_temp_folder

Descrição:
Este módulo é responsável por limpar e criar pastas especificadas. Ele verifica se as pastas 
existem no sistema de arquivos. Caso não existam, elas são criadas. Se existirem, todo o conteúdo 
(incluindo subdiretórios e arquivos) é removido para garantir que as pastas estejam vazias.

Bibliotecas:
- `os`: Utilizada para operações relacionadas ao sistema de arquivos, como verificar a existência de diretórios e manipular arquivos.
- `shutil`: Usada para remover diretórios e seus conteúdos recursivamente.
- `utilities.log_handler`: Contém funções para registrar logs do processo:
  - `log_info`: Registra mensagens informativas.
  - `log_error`: Registra mensagens de erro.

Parâmetros:
- `paths` (list): Lista de caminhos de pastas que devem ser limpas ou criadas.
- `logger` (objeto): Instância do logger utilizada para registrar logs.

Exceções Tratadas:
- `TypeError`: Lançada se o parâmetro `paths` não for uma lista.
- `PermissionError`: Lançada se houver problemas de permissão ao acessar ou manipular os diretórios.
- `Exception`: Captura qualquer outra exceção não prevista durante a execução.

Logs Gerados:
- Log de sucesso para criação ou limpeza de pastas.
- Log detalhado para cada erro encontrado.

Autores:
- [vitor.silva@apsen.com.br]
- [samuel.joseph@apsen.com.br]

Última Modificação:
- 10/12/2024
"""

import os
import shutil
from utilities.log_handler import log_info, log_error

def clear_create_temp_folder(paths, logger):
    """
    Limpa ou cria pastas especificadas.

    Verifica a existência de cada pasta na lista `paths`. Se a pasta não existir, 
    ela é criada. Caso exista, seu conteúdo (arquivos e subdiretórios) é removido, 
    deixando-a vazia.

    Parâmetros:
    - paths (list): Lista de caminhos de pastas a serem limpas ou criadas.
    - logger (objeto): Instância do logger para registro de logs.

    Retorno:
    - None

    Exceções:
    - TypeError: Lançada se o argumento `paths` não for uma lista.
    - PermissionError: Lançada em caso de permissões insuficientes para manipular as pastas.
    - Exception: Captura erros genéricos.
    """

    # teste de arquivo a ser limpado
    paths = [r'C:\Users\User\Desktop\Nova pasta']

    # Verifica se o tipo de dado passado para paths é uma lista
    if not isinstance(paths, list):
        log_error(logger, "clear_create_temp_folder", f"O parametro `path` não é uma lista")
        raise TypeError("O argumento 'paths' deve ser uma lista de strings representando caminhos de pastas.")

    for path in paths:
        try:
            # Se o diretório não existe, cria-o
            if not os.path.exists(path):
                os.mkdir(path)
                log_info(logger, "clear_create_temp_folder", f"Diretório '{path}' criado com sucesso!")
            else:
                # Se o diretório existe, limpa seu conteúdo
                for item in os.listdir(path):
                    item_path = os.path.join(path, item)
                    if os.path.isfile(item_path):
                        os.remove(item_path)  # Remove arquivos
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)  # Remove diretórios e subdiretórios
                log_info(logger, "clear_create_temp_folder", f"Diretório '{path}' limpo com sucesso.")
        except PermissionError as e:
            log_error(logger, "clear_create_temp_folder", 
                      f"Permissão insuficiente para manipular o diretório '{path}': {e}")
        except Exception as e:
            log_error(logger, "clear_create_temp_folder", 
                      f"Erro ao limpar/criar o diretório '{path}': {e}")
