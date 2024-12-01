import csv
with open("films.csv") as file:
    print(file.read())
    
with open("films.csv") as file:
    csv_reader = csv.reader(file)
    for f in csv_reader:
        print(f[0]) #f[0],f[1] hem isim hem turunu alirdik
        #sadece filmlerin isimlerini aldik burada
        print(f"Film adi: {f[0]}, Film türü: {f[1]}, Puani: {f[4]}")
#--------------------------------------------------------------------------------
#dict_reader
from csv import DictReader
with open("films.csv") as file:
    csv_reader = DictReader(file)
    for f in csv_reader:
        print(f) #sozluk olarak erisiriz filmlerimize
        print(f["Title"],f["Genre"])
