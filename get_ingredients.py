#given a url of an AllRecipes recipe, return all ingredients and quantity

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time 
options = FirefoxOptions()
 
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

def get_ingredients(url):

    try:
        driver.get(url)
        time.sleep(3)
        ingredients_list_items = driver.find_elements(By.CSS_SELECTOR, 'li.mntl-structured-ingredients__list-item')

        ingredients = []
        ingredient_names = []  
        for item in ingredients_list_items:
            quantity = item.find_element(By.CSS_SELECTOR, 'span[data-ingredient-quantity="true"]').text.strip()
            unit = item.find_element(By.CSS_SELECTOR, 'span[data-ingredient-unit="true"]').text.strip()
            name = item.find_element(By.CSS_SELECTOR, 'span[data-ingredient-name="true"]').text.strip()

            ingredient = f"{quantity} {unit} {name}"
            ingredients.append(ingredient)
            ingredient_names.append(name)  
    finally:
        driver.quit()

    return ingredients, ingredient_names

url = 'https://www.allrecipes.com/recipe/240784/easy-coleslaw-dressing/' #placeholder url 
ingredients, ingredient_names = get_ingredients(url)
for ingredient in ingredients:
    print(ingredient)
    
for name in ingredient_names:
    print(name)
