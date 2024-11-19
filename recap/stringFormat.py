name="Berke"
surname="Korkut"
age="21"

print("My name is {} {}".format(name,surname))
print("My name is {1} {0}".format(name,surname))
#korkut berke
#print("My name is {n} {s}".format(n=name,s=surname)) farkli bir kullanim sekli

print(f"My name is {name} {surname} and I'm {age} years old.")
#farkli bir formatlama 

number = 5/3
print("the result is {n:1.6}".format(n=number))
#n:n1.6 number'in nokta dahil noktadan sonra 6 hane
#the result is 1.66667
sonuc = " ".join(name)
print(sonuc) # B e r k e
#sonuc = yazi.replace("e","a") = #barka
#-----------------------------------
#tuple
thistuple = (1,2,"alti",False)
#tuplelar () ile kullanilir degistirilemez index islemi yapilir
#-----------------------------------
#{} dictionary 
plakalar = {"izmir":35,
            "istanbul":34
            }

print(plakalar["izmir"])  # 35
#elemanekleme
plakalar["Eskisehir"] = 26
#plakalar.clear() icini bosaltir del plakalar["izmir"] izmiri siler
#plaka = plakalar.copy()
#guncelleme ise plakalar.update({"izmir" :35}) gibi yapilir
#-----------------------------------
#sets indexlenemez siralanmaz

markalar = {"Audi","Mercedes","Bmw","Honda"}
markalar.add("Opel") #remove'u var
#-----------------------------------
x=["python","jacascript"]
y=["python","javascript"]

x=y #bellekte ayni adreste bu bilgiler tutuluyo
y[0]="html"
print(x,y) 
#yani y degisince x de degisiyor