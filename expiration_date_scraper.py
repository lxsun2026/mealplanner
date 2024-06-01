#use Selenium to scrape StillTasty.com and create a 
#table with ingredient names and their shelf lives

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
# options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

def get_expiration_data(url):
    try:
        driver.get(url)
        
        categories = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".images-container.clearfix.red_bg ul > li"))
        )

        for i in range(len(categories)):
            categories = driver.find_elements(By.CSS_SELECTOR, ".images-container.clearfix.red_bg ul > li")  # Re-find categories
            link = categories[i].find_element(By.TAG_NAME, "a")
            category_url = link.get_attribute("href")
            driver.get(category_url)
            
            container2 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-list"))
            )
            
            items = container2.find_elements(By.CSS_SELECTOR, "ul > li")
            
            for j in range(len(items)):
                container2 = driver.find_element(By.CLASS_NAME, "search-list")  
                items = container2.find_elements(By.CSS_SELECTOR, "ul > li") 
                try:
                    food_item = items[j].find_element(By.TAG_NAME, "a")
                    food_item_url = food_item.get_attribute("href")
                    driver.get(food_item_url)
                    expiration_span = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "div.red-arrow > span[style]"))
                    )
                    expiration_text = expiration_span.text.strip()
                    print(expiration_text)  
                except NoSuchElementException:
                    continue  
                finally:
                    driver.back()
                
            driver.back()

    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()

main_url = "https://www.stilltasty.com"
get_expiration_data(main_url)


def parse_expiration_days(expiration_info):
    days = 0
    if "days" in expiration_info:
        days = int(expiration_info.split()[0])
    elif "week" in expiration_info:
        days = int(expiration_info.split()[0]) * 7
    elif "month" in expiration_info:
        days = int(expiration_info.split()[0]) * 30
    elif "year" in expiration_info:
        days = int(expiration_info.split()[0]) * 365
    return days
