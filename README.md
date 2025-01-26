# AUTOMATED CRAWLING AND TESTING FOR A SAMPLE E-COMMERCE WEBSITE
## Objective: 
    Using Selenium for crawling and testing an e-commerce website’s basic functionalities.
## Problem Statement: 
    To design and implement an automated script to crawl an e-commerce website Amazon India and validate specific functionalities. The script focuses on extracting key information from product pages and verifying certain elements on the website.
## Steps to execute the script:
- Ensure you have Python >= 3.9 installed on your system.
- Install the necessary packages by running the following commands:
    - `pip install selenium`
    - `pip install chromedriver-autoinstaller`
- Make sure that Google Chrome is installed and updated on your machine, as the script uses Chrome for automation.
- Clone this repository
- Run `python basic_crawling.py`, this script will open the browser, and simulates actions like searching the product etc., 
- Once the script is executed check the output files. `products_details.csv` file contains the scraped product details in a csv file
- Run `python functional_testing.py`, this script will test valid / invalid inputs, add to cart button, image gallary and description. Logs will be stored in `test_results.log`
- Run `python bonus_task.py`, this script will test for pagination, parallel testing and screen responsive. This is visual testing so please validate by observing chrome automation
- **Note:** amazon.in website tries to block automation by asking for the robot / capcha test. In that case please try again after some time
## Tools and Frameworks:
- Selenium: Used to automate the browser for web scraping, functional testing, and parallel testing. 
- ChromeDriver: Used to interface Selenium with Google Chrome. It’s required to run Selenium scripts in a real browser environment.
- Python: Python is the primary language for scripting the automation.
CSV Module: The csv module is used to write scraped product details.
- Threading Module: Used for implementing parallel testing.
- WebDriverWait: Used for waiting until the page elements are fully loaded, preventing errors due to elements not being available immediately.
- Logging Module (Python): The logging module is used to log functional test results.