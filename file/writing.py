#"w" yazma modu, dosyayı sıfırdan oluşturur ve dosyayı yazar.   
# Eğer dosya zaten varsa, dosyanın içeriğini siler ve dosyayı sıfırdan yazar.
# file = open("info.txt", "w")
# file.write("Berke")
# file.close()
# print(file)

with open("info.txt", "w") as file:
    file.write("Berke\n")
    file.write("Berkay\n")
    print(file)

with(open("info.txt", "r")) as file:
    print(file.read())

#with kodu otomatik kapatma, hata yönetimi ve daha okunaklı kod yazımı sağlar
#------------------------------------------------------------
# "a" ekleme modu, dosyayı sıfırdan oluşturmaz. Eğer dosya yoksa oluşturur ve dosyayı yazar.
# "r+" hem okuma hem yazma modu
with open("info.txt","a") as file:
    file.write("Joshua\n")
    file.write("John\n")
    #en basa ekleme
    
#with open("info.txt","r+") as file: r+ basindan itibaren eklemeye baslar
     # file.write("abigail\n") en basa yazar ama ilk ismi yok eder
