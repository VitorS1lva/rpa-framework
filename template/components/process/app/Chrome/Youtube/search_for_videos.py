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

        if True:
            raise SE("Video nao existe")
        # Open YouTube
        driver.maximize_window()
        driver.get("https://www.youtube.com")
        

        # if 'cpf nao existe':
        #     raise BRE(e)
        
        time.sleep(3)
        # Find the search bar element
        search_box = driver.find_element(By.NAME, "search_query")
        
        # Search for "Python videos"
        search_box.send_keys("Python tutorials")
        search_box.send_keys(Keys.RETURN)
        
        # Wait for search results to load
        time.sleep(3)
        
        # Find video titles
        video_titles = driver.find_elements(By.ID, "video-title")
        
        # Print video titles
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