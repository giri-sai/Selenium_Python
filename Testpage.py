from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.exceptions import 
import time
driver = webdriver.Chrome(executable_path = "C:\sai\ChromeDriver\chromedriver.exe")
driver.get("http://www.flipkart.com")
time.sleep(5)
driver.find_element(By.ID)
print(driver.title)
driver.close()



