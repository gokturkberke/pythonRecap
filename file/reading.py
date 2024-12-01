#open(dosya_adi,dosya_erişme_modu)

# Dosyanın tam yolunu kullanarak açma
f = open("/Users/gokturkberkekorkut/python_software/pythonders1/file/text.txt")
content = f.read()
print(content) # Dosyanın tamamını okur
f.close()

# Aynı dosyayı tekrar açarken de tam yolu kullanın
f = open("/Users/gokturkberkekorkut/python_software/pythonders1/file/text.txt")
print(f.readline())  # İlk satırı okur
print(f.readline())  # İkinci satırı okur
f.seek(5)            # 5. karaktere gider
print(f.readline())  # 5. karakterden itibaren okur (ci satir)
f.close()
