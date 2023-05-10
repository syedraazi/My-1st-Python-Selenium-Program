import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options=webdriver.ChromeOptions()                                   #Used to hold the window from closing
options.add_experimental_option("detach",True)                      #Used to hold the window from closing
serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")      # Use this statement in Selenium 4
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

#Extract and Validate the URL
time.sleep(5)
url=driver.current_url
if url=="https://itera-qa.azurewebsites.net/home/automation":
    print("URL is valid:- "+ url)
else:
    print("Incorrect URL")

#Extract the title
time.sleep(5)
title=driver.title
print("Title is: "+title)

# Find all the elements and perform actions
time.sleep(5)
driver.find_element(By.ID,"name").send_keys("SRS")
driver.find_element(By.ID,"phone").send_keys("9792365432")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("abc@gmail.com")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("abc123")
driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("ABC Street,India")
driver.find_element(By.XPATH,"//button[@name='submit']").click()

time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='male']").click()
driver.find_element(By.XPATH,"//input[@id='tuesday']").click()

time.sleep(5)
driver.find_element(By.XPATH,"//option[@value='2']").click()
# travelplace=driver.find_element(By.XPATH,"//select[@class='custom-select']")
# place=Select(travelplace)
# place.select_by_value("Spain")

time.sleep(5)
driver.find_element(By.XPATH,"//label[@for='1year']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//label[@for='selenium']").click()

#Close the browser at the end.
time.sleep(5)
driver.close()
input("Press Enter to close the browser window...")