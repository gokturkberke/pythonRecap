import os

# Python dosyasının bulunduğu klasörü bul
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "text.txt")

# Dosyayı aç ve oku
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File not found: {file_path}")
#--------------------------------------------
with open("text.txt", "r") as file:
    print(file.read()) # Dosyanın tamamını oku
    print(file.tell()) # Dosyanın kaçıncı byte'ında olduğunu gösterir
    print(file.read(20)) # İlk 20 karakteri oku
    print(file.tell()) # 21