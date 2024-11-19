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
