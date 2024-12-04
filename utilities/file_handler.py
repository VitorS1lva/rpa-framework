import os
import shutil

def clear_or_create_folder(folder_path):
    """Limpa ou cria uma pasta."""
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)
