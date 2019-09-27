import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()  
chrome_options.add_argument("start-fullscreen")
chrome_options.add_argument("--headless") 

driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)

def check_menu(hall):
    url = "https://dining.unc.edu/locations/" + encode_hall(hall) + "/?date=" + str(datetime.date.today())

    driver.get(url)

    tabs = driver.find_elements_by_class_name("c-tabs-nav__link-inner")
    elements = driver.find_elements_by_class_name("show-nutrition")

    food = {}

    for tab in tabs:
        tab.click()
        time.sleep(0.5)
        food[tab.text] = {}
        for element in elements:
            if element.is_displayed():
                food[tab.text][element.text] = None

    driver.close()
    
    return food

def get_protein(hall):
    url = "https://dining.unc.edu/locations/" + encode_hall(hall) + "/?date=" + str(datetime.date.today())

    driver.get(url)

    tabs = driver.find_elements_by_class_name("c-tabs-nav__link-inner")
    elements = driver.find_elements_by_class_name("show-nutrition")

    food = {}

    for tab in tabs:
        tab.click()
        time.sleep(0.5)
        protein_values = {}

        for element in elements:
            if element.is_displayed():
                element.click()
                time.sleep(0.4)
                for i in range(3):
                    try:
                        protein = driver.find_elements_by_tag_name("th")[-1].text[8:-2]
                        protein_values[element.text] = protein
                        break
                    except:
                        print("Attempt #" + str((i + 1)) + " to fetch protein data for " + element.text + " failed.") 
                        time.sleep(0.5)

                webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                time.sleep(0.3)
    
        food[tab.text] = protein_values

    driver.close

    return food

def encode_hall(hall):
    switcher = {
        "chase": "chase",
        "lenoir": "top-of-lenoir"
    }
    return switcher.get(hall)