# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib

# NOTE: Check robots.txt to confirm which elements of the site can be scraped

# Initialization
driver = webdriver.Firefox()
driver.maximize_window()

# Website address
driver.get('https://www.pap.pl')

# Accepting cookies
cookies = driver.find_element(By.XPATH,
                              "/html/body/div/div[3]/div/div/div/div/div/div[1]")
cookies.click()

# Changing the site's language to English
eng = driver.find_element(By.XPATH,
                          "/html/body/div/header/nav/div/div[2]/ul[2]/li[3]/a")
eng.click()

# Business section
business = driver.find_element(By.XPATH, 
                               "/html/body/div/header/nav/div/div[2]/nav/ul/li[3]/a")
business.click()

# Headings to a list
headings = driver.find_elements(By.CLASS_NAME, "title")
titles = [] 
for h in headings:
    titles.append(h.text)
print(titles)

# Images download
imgs = []
webelement_img = driver.find_elements(By.XPATH, '//img')
for elements in webelement_img:
    new = elements.get_attribute("src")
    if new[-4:] == ".png":
        urllib.request.urlretrieve(new, filename = new.split("/")[-1])
    else:
        new1 = new.split("?itok")[0]
        urllib.request.urlretrieve(new, filename = new1.split("/")[-1])
    
# Scroll down and get the last page
driver.execute_script("window.scrollTo(0, 1500)") 
last_page = driver.find_element(By.XPATH, 
                                "/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/nav/ul/li[6]/a")
last_page.click()

url = str(driver.current_url)
print(f"Last page: {url[-2:]}")

# End the session
time.sleep(2)
driver.quit()
