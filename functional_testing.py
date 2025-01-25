from selenium import webdriver 
from selenium.webdriver.common.by import By 
import logging

# Configure logging
logging.basicConfig(
    filename="test_results.log",  # Name of the log file
    level=logging.INFO,           # Log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

options = webdriver.ChromeOptions()  
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

def test_valid_inputs():
    driver.get("https://www.amazon.in")
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("Amazon Echo Dot")  # Types the product name in the search bar
    search_box.submit()
    driver.implicitly_wait(5)
    products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
    if len(products) > 0:
        logging.info("Test valid inputs: PASS")
    else:
        logging.info("Test valid inputs: FAIL")

def test_invalid_inputs():
    driver.get("https://www.amazon.in")
    search_box_invalid = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box_invalid.clear()
    search_box_invalid.send_keys("randomtext") 
    search_box_invalid.submit()
    driver.implicitly_wait(5)
    products_invalid = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
    if len(products_invalid) == 0:
        logging.info("Test invalid inputs: PASS")
    else:
        logging.info("Test invalid inputs: FAIL")

def test_add_to_cart():
    driver.get("https://www.amazon.in")
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("Amazon Echo Dot")  # Types the product name in the search bar
    search_box.submit()
    driver.implicitly_wait(5)
    product = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')[0]
    product_url = product.find_element(By.TAG_NAME,"a").get_attribute("href")
    driver.get(product_url)
    driver.implicitly_wait(5)
    try:
        driver.find_element(By.XPATH, '//input[@id="add-to-cart-button"]')
        logging.info("Add to Cart button: PASS")
    except Exception as e:
        logging.error(f"Add to Cart button: FAIL - {e}")

def test_description():
    driver.get("https://www.amazon.in")
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("Amazon Echo Dot")  # Types the product name in the search bar
    search_box.submit()
    driver.implicitly_wait(5)
    product = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')[0]
    product_url = product.find_element(By.TAG_NAME,"a").get_attribute("href")
    driver.get(product_url)
    driver.implicitly_wait(5)
    try:
        driver.find_element(By.XPATH, '//div[@id="feature-bullets"]')
        logging.info("Description section: PASS")
    except Exception as e:
        logging.error(f"Description section: FAIL - {e}")

def test_image_gallary():
    driver.get("https://www.amazon.in")
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("Amazon Echo Dot")  # Types the product name in the search bar
    search_box.submit()
    driver.implicitly_wait(5)
    product = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')[0]
    product_url = product.find_element(By.TAG_NAME,"a").get_attribute("href")
    driver.get(product_url)
    driver.implicitly_wait(5)
    try:
        driver.find_element(By.XPATH, '//li[@data-csa-c-action="image-block-alt-image-hover"]')
        logging.info("Image gallery functionality: PASS")
    except Exception as e:
        logging.error(f"Image gallery functionality: FAIL - {e}")

test_valid_inputs()
test_invalid_inputs()
test_add_to_cart()
test_description()
test_image_gallary()

driver.quit()
