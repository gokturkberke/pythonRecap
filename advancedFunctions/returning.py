def usalma(number):
    def inner(power):
        return number ** power
    
    return inner

x = usalma(5)
y = usalma(3)
print(x(3)) #125

print(y(4)) #81

def islem(islem_adi):
    def toplam(*args): #parametre sayisini bilmiyoruz
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islem_adi == "toplama":
        return toplam
    else:
        return carpma
toplama = islem("toplama")
print(toplama(1,2,3,4,5)) #15

carpma = islem("carpma")
print(carpma(1,2,3,4,5)) #120
#-----------------------------------------------------
#func_parameters

def toplama(a,b):
    return a + b
def cikarma(a,b):
    return a - b
def carpma(a,b):
    return a * b
def bolme(a,b):
    return a / b

def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi == "toplama":
        print(f1(2,3))
    elif islem_adi == "cikarma":
        print(f2(5,3))
    elif islem_adi == "carpma":
        print(f3(3,4))
    elif islem_adi == "bolme":
        print(f4(10,2))
    else:
        print("Gecersiz islem")

islem(toplama,cikarma,carpma,bolme,"toplama") #5
