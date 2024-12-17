import sys
import os


# Adicione o caminho raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from utilities.treat_errors import BRE, SE
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

status = "SUCESSO"
error_message = ""


def search_for_videos(driver):
    try:

        # if True:
        #     raise SE("Video nao existe")
        
        if True:
            raise BRE("CPF inexistente")
        # Open YouTube
        driver.maximize_window()
        driver.get("https://www.youtube.com")
        
        time.sleep(3)
        search_box = driver.find_element(By.NAME, "search_query")

        search_box.send_keys("Python tutorials")
        search_box.send_keys(Keys.RETURN)
        time.sleep(6)
        video_titles = driver.find_elements(By.ID, "video-title")
        
        for title in video_titles[:10]:  # Limit to first 10 results
            print(title.text)
        
        status = "SUCCESS"
        error_message = ""
        return status, error_message
    except BRE as e:
        status = "BUSINESS_RULE_EXCEPTION"
        error_message = e
        return status, error_message
    except SE as e:
        status = "SYSTEM_EXCEPTION"
        error_message = e
        return status, error_message