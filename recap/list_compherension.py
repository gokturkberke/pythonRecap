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
#----------------------------------------
def selamla(isim="Kullanici",mesaj = "Hos geldiniz"): #def value ekliyoruz(herhangi bir sey girmezsek diye)
    print(f"{mesaj} {isim}")
    
selamla("Berke","Merhaba")
selamla("gokce") #hos geldiniz gokce
selamla() #hos geldiniz Kullanici(hata vermez hic bir sey girmesek bile)
#----------------------------------------
#args
numbers = [5,15,20,25]

# def topla(a,b):
#     return a+b

# def topla(a,b,c):
#     return a+b+c

# def topla(sayilar):
#     sonuc=0
#     for i in sayilar:
#         sonuc+=i
#     return f"Sayilarin toplami : {sonuc}"

# print(topla(numbers))

def topla(*args):
    sonuc=0
    for i in args:
        sonuc+=i
    return f"Sayilarin toplami : {sonuc}"
print(topla(5,15,20))
#fonksiyona değişken sayıda pozisyonel argüman geçirmeyi sağlar. Argümanlar bir tuple olarak fonksiyona iletilir.
#----------------------------------------
#kwargs fonksiyona değişken sayıda anahtar-değer çiftleri (keyword arguments) geçirmeyi sağlar. Argümanlar bir dictionary olarak fonksiyona iletilir.

def userInfo(**kwargs):
    print(type(kwargs)) #dict
    print(kwargs)

#soyle de yazabiliriz

def userInfo(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
        print("\n")
userInfo(username="berke",password ="123456",email="berkekorkut@gmailcom") #key value
#----------------------------------------
