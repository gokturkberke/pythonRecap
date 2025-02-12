name="Berke"
surname="Korkut"
age="21"

print("My name is {} {}".format(name,surname))
print("My name is {1} {0}".format(name,surname))
#korkut berke
#print("My name is {n} {s}".format(n=name,s=surname)) farkli bir kullanim sekli

print(f"My name is {name} {surname} and I'm {age} years old.")
#farkli bir formatlama 

gel_yaz = " gelecegi_yazanlar "
gel_yaz.strip() #bosluklari siler kelimedeki(default)
gel_yaz = "*gelecegi_yazanlar*"
gel_yaz.strip("*") #kelimenin basindaki ve sonundaki * siler

number = 5/3
print("the result is {n:1.6}".format(n=number))
#n:n1.6 number'in nokta dahil noktadan sonra 6 hane
#the result is 1.66667

sonuc = " ".join(name) #her bir karakter arasina bosluk koyar
print(sonuc) # B e r k e
#sonuc = name.replace("e","a") = #barka
#-----------------------------------
#tuple
thistuple = (1,2,"alti",False)
#tuplelar () ile kullanilir degistirilemez index islemi yapilir
#-----------------------------------
#{} dictionary degistirilebilir ama index islemi yapilamaz
plakalar = {"izmir":35,
            "istanbul":34
            }

#eleman plakalar["izmir"]  seklinde secilir sozluklerde

print(plakalar["izmir"])  # 35
#elemanekleme
plakalar["Eskisehir"] = 26
#plakalar.clear() icini bosaltir del plakalar["izmir"] izmiri siler
#plaka = plakalar.copy()
#guncelleme ise plakalar.update({"izmir" :35}) gibi yapilir
#-----------------------------------
#sets indexlenemez degistirilebilir degerler essizdir

markalar = {"Audi","Mercedes","Bmw","Honda"}
markalar.add("Opel") #remove'u var
#discard fonksiyonu farkli olarak hata vermez remove da eleman yoksa hata verir
#-----------------------------------
x=["python","jacascript"]
y=["python","javascript"]

x=y #bellekte ayni adreste bu bilgiler tutuluyo
y[0]="html"
print(x,y) 
#yani y degisince x de degisiyor

#listelerde insert indexe gore append listenin sonuna ekler
#remove son elemani siler pop indexe gore siler 
#-----------------------------------
x=y=[1,2,3,4]
z=[1,2,3,4]
print(x is z) #ayni olmalarina ragmen false yazdirir cunku adresleri farkli
#-----------------------------------
r = range(10)

sonucc = list(r) # [0,1...9]

diller = ["Python","Javascript","Flutter"]

index = 0
for i in diller:
    print(f"{index+1} - {diller[index]}")
    index += 1
    
#obje = enumerate(diller)

#print(type(obje)) -> enumarate

for index,value in enumerate(diller):
    print(f"{index}-{value}")

#for ile yaptigimiz seyin aynisini yapar
#enumarate bir iterable uzerinde döngü kurarken her elemanın indeksini ve değerini aynı anda elde etmemizi saglar
#for index, char in enumerate("Python"):
  #  print(f"{index}: {char}")
# 0: P
# 1: y
# 2: t
# 3: h
# 4: o
# 5: n
#-----------------------------------
#zip metodu iki listenin elemanlarini birlestirmek icin kullanilir
list1 = [1, 2, 3]
list2 = ['a', 'b']

zipped = zip(list1, list2)
print(list(zipped))
#eger ikisinin uzunluk farkliysa kisaya gore birlestirir
#[(1, 'a'), (2, 'b')]
