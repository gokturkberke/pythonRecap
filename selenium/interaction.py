import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Safari()

driver.get("https://www.n11.com")

searchInput = driver.find_element(By.ID, "searchData")
searchInput.send_keys("telefon")
searchInput.send_keys(Keys.ENTER)
time.sleep(3)

login = driver.find_element(By.LINK_TEXT, "Giriş Yap")
login.click()
time.sleep(2)

emailInput= driver.find_element(By.ID, "email")
emailInput.send_keys("gokturkberke1907@gmail.com")
time.sleep(2)
passwordInput=driver.find_element(By.ID, "password")
passwordInput.send_keys("123456")
time.sleep(2)
passwordInput.send_keys(Keys.ENTER)
time.sleep(2)
driver.close()  