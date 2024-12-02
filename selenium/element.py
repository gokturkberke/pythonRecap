from selenium import webdriver
from selenium.webdriver.common.by import By #by sinifini ice aktarir bu sinif elementleri bulmak icin kullanilan yontemleri icerir

driver = webdriver.Safari()
driver.get("https://www.trendyol.com/apple/yenilenmis-iphone-11-64-gb-beyaz-a-grade-p-752408147?boutiqueId=61&merchantId=599213")

title = driver.find_element(By.CLASS_NAME, "pr-new-br").text #pr-new-br isimli classi buluyoruz
print(title)  #Çıktı: Apple Yenilenmiş iPhone 11 64 GB Beyaz A Grade
#incele(inspect) diyip css kodlarindan buluyoruz sinif isimleriin
search_input = driver.find_element(By.CLASS_NAME, "search-box").get_attribute("placeholder")
print(search_input) #Çıktı: Aramak istediğiniz ürün, kategori veya markayı yazınız

driver.close()