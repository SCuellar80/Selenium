# Headless needs Options library
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# Headless is enabled or disabled with Options()
chrome_options = Options()
chrome_options.add_argument("--headless")  # enable headless, comment it to disable it

# Creates the driver with Options argument
# driver = webdriver.Chrome() not used
driver = webdriver.Chrome(chrome_options)

# Open the browser but you will not see anything running (but you can see it in the process)
driver.get("https://www.google.com")

# Set a breakpoint here to check that the browser is not visible until you comment --headless argument
driver.quit()
