from selenium import webdriver  
from selenium.webdriver.common.by import By
import threading

print("BONUS_TASK 1 :Implementing a script to crawl multiple pages of search results.")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  
driver = webdriver.Chrome(options=options)

driver.get("https://www.amazon.in") 
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Amazon Echo Dot")
search_box.submit()

driver.implicitly_wait(5)

while True:
    try:
        # Locate all product elements on the current page
        products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
        
        # Try to find and click the "Next" button
        next_button = driver.find_element(By.CSS_SELECTOR, ".s-pagination-next")
        if "s-pagination-disabled" not in next_button.get_attribute("class"):
            next_button.click()
            driver.implicitly_wait(5)
        else:
            print("Next button is disabled. Exiting.")
            break
    except Exception as e:
        print("No more pages to crawl or error occurred:", e)
        break

# Close the browser
driver.quit()

print("BONUS_TASK 2 :Using Selenium Grid to demonstrate parallel testing.") 
# Function for each browser instance
def search_product_in_browser(browser_index):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Start the browser in full-screen mode
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.amazon.in")
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("Amazon Echo Dot")  # Types the product name in the search bar
    search_box.submit()
    driver.implicitly_wait(5)
    products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
    print(f"Browser {browser_index} found {len(products)} products.")
    driver.quit()

# Create a list of threads
threads = []
for i in range(2):  # Run tests in 3 parallel browser instances
    t = threading.Thread(target=search_product_in_browser, args=(i+1,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("BONUS_TASK 3 :Testing responsiveness of the website by simulating different screen sizes.")
# Function to test responsiveness for a specific screen size
def test_responsiveness(width, height):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Start the browser in full-screen mode
    driver = webdriver.Chrome(options=options)

    try:
        # Simulate screen size
        driver.set_window_size(width, height)
        print(f"Screen size set to {width}x{height}")
        
        driver.get("https://www.amazon.in")
        driver.implicitly_wait(5)

        # Perform a search action
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys("Amazon Echo Dot")  # Types the product name in the search bar
        search_box.submit()

        driver.implicitly_wait(5)

        # Test the responsiveness by checking for specific elements
        results = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
        print(f"Found {len(results)} products.")

    finally:
        driver.quit()

# Define different screen sizes to simulate
screen_sizes = [
    (360, 640),  # Mobile size
    (768, 1280),  # Tablet size
    (1024, 768),  # Desktop size (small)
    (1366, 768),  # Common desktop size
    (1920, 1080),  # Full HD desktop size
]

# Test responsiveness for each screen size
for width, height in screen_sizes:
    test_responsiveness(width, height)