def sayac(max):
    sayi = 1
    
    while sayi <=max:
        yield sayi #sayiyi bellekte tutmadan donduruyor
        sayi += 1

iterator = sayac(20)
#print(next(iterator)) #sadece gostermeye yarar bellekte tutmaz

#for i in iterator:
    #print(i)

sonuc = list(iterator)
print(sonuc)

liste = (i for i in range(1,11))
print(next(liste))