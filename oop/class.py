#Class
#Instance , Object

class Arac:
    pass 

arac1 = Arac()
print(type(arac1)) # <class '__main__.Arac'>

class Products:
    pass

p1=Products()
p2=Products()
p3=Products()
listProducts = [p1,p2,p3]
for p in listProducts:
    print(p) 
#----------------------------
class Product:
    def __init__(self,name,price,isActive=True): #isactive default olarak true
        self.name = name
        self.price = price
        self.isActive = isActive
        print("Product Created")

p1 = Product("Mercedes A", "200000")
p2 = Product("BMW 3.20", "150000",False)
print(p1.name,p1.price,p1.isActive) #Mercedes A 200000 True
print(p2.name,p2.price,p2.isActive) #   BMW 3.20 150000 False
