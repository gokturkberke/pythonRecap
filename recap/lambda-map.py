#Lambda fonksiyonlarılambda anahtar kelimesi ile tanımlanır ve genellikle kısa süreli kullanım için tasarlanmıştır.
sayilar = [1, 2, 3, 4, 5]
kareler = list(map(lambda x: x ** 2, sayilar))
print(kareler)  # Çıktı: [1, 4, 9, 16, 25]

#lambda arguments : expression

# map fonksiyonu, bir fonksiyon ve bir iterable (örneğin, liste) alır ve bu fonksiyonu iterable'ın her bir elemanına uygular.
#Bir listenin veya başka bir iterable'ın her elemanına aynı işlemi uygulamak istediğinizde
a = [1, 2, 3]
b = [4, 5, 6]
toplam = list(map(lambda x, y: x + y, a, b))
print(toplam)  # Çıktı: [5, 7, 9]

#filter fonksiyonu belirli bir kosula gore filtreleme yapar.
yaslar = [7,15,18,27,36]

def yetiskinmi(x):
    if x>=18:
        return True
    else:
        return False
    
sonuc = list(filter(yetiskinmi,yaslar))
#sonuc = list(filter(lambda x: x>=18,yaslar)) aynisini tek satirda yazabiliriz.


print(sonuc) #Çıktı: [18, 27, 36]

def cift_mi(x):
    return x % 2 == 0

sayilar = [1, 2, 3, 4, 5, 6]
cift_sayilar = list(filter(cift_mi, sayilar))
print(cift_sayilar)  # Çıktı: [2, 4, 6]
#--------------------------------------------------------------------------------
#any - all fonksiyonları
sonuc = all([True , False,True])
print(sonuc) #False(hepsinin true olmasi lazim true olmasi icin)
#any ise herhangi birinin true olmasi true olmasina yeterlidir.

sayilar = [0,1,4,7,8,10,15]
sonuc = [bool(sayi) for sayi in sayilar]#bool fonksiyonu sayinin 0 olup olmadigini kontrol eder.
print(sonuc) #False, True, True, True, True, True, True
sonuc = any([bool(sayi) for sayi in sayilar]) #herhangi birinin true olmasi yeterlidir.

isimler = ["ali","arda","mehmet","didem"]

sonuc = [isim[0] == "a" for isim in isimler]  #true true false false 
sonuc = any([isim[0] == "a" for isim in isimler]) #herhangi birinin true olmasi yeterlidir.
#--------------------------------------------------------------------------------
araclar = [
    {"title" : "Audi A4", "price" : 30000},
    {"title" : "BMW 5", "price" : 40000},
    {"title" : "Mercedes C180", "price" : 25000}
]
sonuc = min(araclar, key = lambda x : x["price"])
print(sonuc) #Çıktı: {'title': 'Mercedes C180', 'price': 25000}
sonuc = min(araclar, key = lambda x : x["price"])["title"] #Çıktı: Mercedes C180
#--------------------------------------------------------------------------------
urunler = [
    {"title" : "kitap a", "price" : 200},
    {"title" : "kitap b", "price" : 300},
    {"title" : "kitap c", "price" : 400}
]

toplamFiyat = sum([urun["price"] for urun in urunler])
sonuc = toplamFiyat
print(sonuc) #Çıktı: 900
#--------------------------------------------------------------------------------