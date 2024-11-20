sayilar= []

for i in range(10):
    sayilar.append(i)
print(sayilar)
#bunu su sekil de yapabiliriz

sayilar = [i for i in range(10)]
sayilar = [i*2 for i in range(10)] #i'nin 2 kati olan degerler ile liste olusturuyoruz


liste = [3,8,4,12,40]

sayilar = [i*2 for i in liste]

print(sayilar)

isim = "berke"

sonuc = [a.upper() for a in isim] #her bir harf liste oldu 
print(sonuc)

#condition with compherension

numbers = [1,3,7,12,22,34]
sonuc = []

for sayi in sayilar:
    if (sayi % 2 == 0):
        sonuc.append(sayi)
        
sonuc = [sayi for sayi in sayilar if sayi%2 == 0]
#else kullanmak icin
sonuc = [sayi if sayi%2 == 1 else "cift sayi" for sayi in sayilar]
