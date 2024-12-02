from selenium import webdriver

# Launch Safari browser
driver = webdriver.Safari()

# Open a website
driver.get("https://example.com")

# Example: Print the page title
print(driver.title)

# Close the browser
driver.quit()
