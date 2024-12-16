from PIL import ImageGrab
from datetime import datetime
from utilities.log_handler import *

def take_screenshot(logger):
    try:
        time = datetime.now().strftime(f"%d_%m_%Y_%H_%M_%S")
        screenshot = ImageGrab.grab()
        screenshot.save(f"logs/Screenshots/{time}.png")
        screenshot.close()
    except PermissionError as e:
        log_info(logger, "take_screenshot", f"Erro de permissão ao tentar tirar print da tela - {e}")
        raise (f"take_screenshot - Erro de permissão - {e}")
    except SystemError as e:
        log_info(logger, "take_screenshot", f"Erro de sistema ao tentar tirar print da tela - {e}")
        raise (f"take_screenshot - Erro do sistema - {e}")
    except Exception as e:
        log_info(logger, "take_screenshot", f"Erro genrico ao tentar tirar print da tela - {e}")
        raise (f"take_screenshot - Erro generico - {e}")