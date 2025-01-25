from selenium import webdriver  
from selenium.webdriver.common.by import By  
import csv


# Configure browser options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized") 
driver = webdriver.Chrome(options=options)

driver.get("https://www.amazon.in")  
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Amazon Echo Dot")  
search_box.submit()

driver.implicitly_wait(5)

products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
with open("products_details.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price", "Rating", "URL"])
    for product in products:
        name = product.find_element(By.TAG_NAME, "h2").text
        price = ""
        try:
            price = product.find_element(By.CSS_SELECTOR, ".a-price-whole").text
        except:
            pass
        ratings = ""
        try:
            ratings = product.find_element(By.CSS_SELECTOR, ".a-icon-alt").get_attribute("innerHTML")
        except:
            pass
        url = product.find_element(By.TAG_NAME, "a").get_attribute("href")
        # Write the product details to the CSV
        writer.writerow([name, price, ratings, url])
            
# Close the browser
driver.quit()

print("Product details saved to 'products_details.csv'")