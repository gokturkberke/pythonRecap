from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://www.python.org/")

blog_times = driver.find_elements(By.CSS_SELECTOR, ".blog-widget time")
blog_names = driver.find_elements(By.CSS_SELECTOR, ".blog-widget a")
blogs = {}
for i in range(len(blog_names)):
    blogs[i] = {
        "time": blog_times[i].text,
        "name": blog_names[i].text
    }

for time in blog_times:
    print(time.text) #2024-11-25,2024-11-19 ... 
for name in blog_names:
    print(name.text) #PSF Board Retreat 2024 , Python 3.14.0 alpha 2 released ...
    
print(blogs) 
driver.close()