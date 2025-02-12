def sayac(max):
    sayi = 1
    
    while sayi <=max:
        yield sayi #sayiyi bellekte veri tutmadan donduruyor
        #yield, fonksiyonun bir sonraki çağrıda kaldığı yerden devam etmesini sağlar. Eğer return kullansaydık, fonksiyon bir değer döndürür ve tamamen sona ererdi. Ama yield sayesinde iterator gibi çalışır.
        sayi += 1

iterator = sayac(20) #generator objesi
#print(next(iterator)) #next(iterator) her çağrıldığında bir sonraki sayıyı döndürür.

#for i in iterator:
    #print(i)

sonuc = list(iterator)
print(sonuc)

liste = (i for i in range(1,11)) #generator comprehension örneğidir.
print(next(liste)) #1