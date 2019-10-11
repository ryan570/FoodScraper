import datetime
import platform
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from foodscraper.cache import read_data, append_data
from foodscraper.item import Item, create_item

options = Options()
options.add_argument('--headless')
options.add_argument('start-fullscreen')

path = '/home/ryan/Projects/FoodScraper/chromedriver' if platform.system() == 'Linux' else 'chromedriver.exe'

driver = webdriver.Chrome(path, options=options)

def fetch_nutrition(hall):
    menu = check_menu(hall)
    cache = read_data('cache.json')
    nutrition = {}
    unknown = []

    for timeslot in menu:
        current_list = []
        for item in menu[timeslot]:
            if item in list(cache.keys()):
                current = create_item(item, cache[item])
            else:
                current = Item(item, 0, 0, 0)
                unknown.append(item)
            current_list.append(current)
        nutrition[timeslot] = current_list
    
    if unknown:
    
        url = "https://dining.unc.edu/locations/" + encode_hall(hall) + "/?date=" + str(datetime.date.today())

        driver.get(url)

        updated = {}

        tabs = driver.find_elements_by_class_name("c-tabs-nav__link-inner")

        for tab in tabs:
            tab.click()
            time.sleep(1)

            for item in unknown:
                try:
                    element = driver.find_element_by_link_text(item.strip())
                except:
                    break
                if element.is_displayed():
                    element.click()
                    time.sleep(1)

                    for i in range(3):
                        try:
                            info = driver.find_elements_by_tag_name("th")
                            updated[item] = {
                                "calories": info[1].text[9:],
                                "sodium": info[7].text[7:-3],
                                "protein": info[-1].text[8:-2]
                            }
                            break
                        except:
                            print("Attempt #" + str((i + 1)) + " to fetch nutrition data for " + element.text + " failed.") 
                            time.sleep(0.5)

                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    time.sleep(0.5)
        driver.close

        append_data(updated)

        for food_list in nutrition.values():
            for item in food_list:
                if item.name in updated:
                    info = updated[item.name]
                    item = Item(item, info["calories"], info["sodium"], info["protein"])

    return nutrition

def check_menu(hall):
    url = "https://dining.unc.edu/locations/" + encode_hall(hall) + "/?date=" + str(datetime.date.today())

    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    tab_labels = soup.find_all('div', class_='c-tabs-nav__link-inner')
    tab_contents = soup.find_all('div', class_='c-tab__content')

    labels = [tab.text for tab in tab_labels]

    menu = {}

    for index,tab in enumerate(tab_contents):
        content = []
        current = tab.find_all('a', class_='show-nutrition')
        menu[labels[index]] = [link.text for link in current]

    return menu

def encode_hall(hall):
    switcher = {
        "chase": "chase",
        "lenoir": "top-of-lenoir"
    }
    return switcher.get(hall)