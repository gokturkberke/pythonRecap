import math

sonuc = dir(math)
print(sonuc) #we can see all the functions in math module

#math.sqrt(36) => 6.0
#math.factorial(5) => 120
#math.floor(5.9) => 5 asagi yuvarlama
#math.ceil(5.1) => 6 yukari yuvarlama

from math import * #import all functions from math module
#artik marh kullanmadan direk fonksiyonlari kullanabiliriz
sonuc = sqrt(36)
sonuc = factorial(5)

#------------------------------------------------
import random
#sonuc = dir(random)

sonuc = random.random() #0.0 - 1.0 arasinda rastgele sayi uretir
# sonuc = random.random() * 10 = 0.0 - 10.0 arasinda rastgele sayi uretir

result = int(random.uniform(1,10)) #1.0 - 10.0 arasinda rastgele tam sayi uretir
#uniform araligi kendimiz giriyoruz tam sayi olmasini istersek int ekleriz basina

result = random.randint(1,100) #1 - 100(100 dahil degil) arasinda rastgele tam sayi uretir

users = ["berke", "ali", "veli", "ayse"]
name = "Levent"

sonuc = users[random.randint(0, len(users)-1)] #random bir isim secmek icin
sonuc = random.choice(users) #random bir isim secmek icin
sonuc = random.choice(name) #random bir harf secmek icin

liste = list(range(10))
random.shuffle(liste) #listeyi karistirir
print(liste) 

liste = range(100)
sonuc = random.sample(liste, 5) #100 elemanli listeyi 5 elemanli random bir liste olusturur