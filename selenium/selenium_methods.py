import time
from selenium import webdriver

# Safari tarayıcısını başlat
driver = webdriver.Safari()

# Web sitesine git
url = "https://www.instagram.com/gokturkk_berkee/"
driver.get(url)

# Sayfanın yüklenmesi için bekle
time.sleep(5)

# Ekran görüntüsü al
driver.save_screenshot("instagram.png")


# Tarayıcıyı kapat
driver.quit() #tum tarayiciyi ve acik tum pencereleri kapatir

#driver.back() # Bir önceki sayfaya gitmek için
#driver.forward() # Bir sonraki sayfaya gitmek için
#driver.close() # Sadece aktif pencereyi kapatir