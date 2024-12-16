from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

def initialize_chrome():
    try:
        return webdriver.Chrome()  
    
    except PermissionError as e:
        raise e
    
    except ConnectionError as e:
        raise e
    
    except ConnectionRefusedError as e:
        raise e
    
    except SystemError as e:
        raise e

    except Exception as e:
        # log_error(logger, "Initialize All Applications", f"Erro ao inicializar aplicações: {e}")
        raise e