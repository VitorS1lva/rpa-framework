import sys
import os

# Adicione o caminho raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search_for_videos(driver):
    try:
        # Open YouTube
        driver.get("https://www.youtube.com")
        driver.maximize_window()
        
        time.sleep(3)
        # Find the search bar element
        search_box = driver.find_element(By.NAME, "search_query")
        
        # Search for "Python videos"
        search_box.send_keys("Python tutorials")
        search_box.send_keys(Keys.RETURN)
        
        # Wait for search results to load
        time.sleep(5)
        
        # Find video titles
        video_titles = driver.find_elements(By.ID, "video-title")
        
        # Print video titles
        for title in video_titles[:10]:  # Limit to first 10 results
            print(title.text)
        
    finally:
        # Close the browser
        driver.quit()
