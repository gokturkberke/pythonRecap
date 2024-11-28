import os

sonuc = os.name # posix (macos)

#etkin dizin ogrenme
sonuc = os.getcwd() # /Users/gokturkberkekorkut/python_software/pythonders1
print(sonuc)

#dizin degistirme
#os.chdir('/Users/gokturkberkekorkut/python_software') bir ust dizine cikar
#os.chdir("..") bir ust dizine cikar os.chdir("../..") iki ust dizine cikar
os.chdir("//Users") # /Users a gider direkt

#klasor olusturma   
#os.mkdir("deneme") # deneme adinda klasor olusturur
#os.makedirs("deneme2/deneme3") # deneme2 altina deneme3 adinda klasor olusturur(ic ice klasor)
#os.rename("deneme2", "deneme4") # deneme2 adindaki klasoru deneme4 olarak degistirir
#os.rmdir("deneme") # deneme adindaki klasoru siler
#os.removedirs("deneme4/deneme3") # deneme4 altindaki deneme3 klasorunu de siler(ikisini de siler)

#listeleme
sonuc = os.listdir() 
sonuc = os.listdir("/Users") # /Users klasorundeki dosya ve klasorleri listeler
print(sonuc)
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)
print(dosya) # all python files in the current directory

#dosya hakkinda bilgi alma

sonuc = os.stat("errors.py")