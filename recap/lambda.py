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