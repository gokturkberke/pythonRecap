def selamlama(fn):
    def inner(ad):
        print("Programa hosgeldiniz")
        fn(ad)
        print("gorusmek uzere")
    return inner

@selamlama # Decorator
def gunaydin(ad):
    print("Gunaydin" + ad)
   
@selamlama    
def iyigunler(ad):
    print("Iyi gunler" + ad)
 
@selamlama   
def iyiaksamlar(ad):
    print("Iyi aksamlar" +  ad)



gunaydin("Berke") # Programa hosgeldiniz Gunaydin Berke gorusmek uzere
iyigunler("Mehmet") # Programa hosgeldiniz Iyi gunler Mehmet gorusmek uzere
iyiaksamlar("Naz") # Programa hosgeldiniz Iyi aksamlar Naz gorusmek uzere
#--------------------------------------------------------------------------------
def fn_x2(func):
    def wrapper_fn_x2(*args, **kwargs):
        func(*args, **kwargs)
        func(*args,**kwargs) #iki kere cagirir
    return wrapper_fn_x2

@fn_x2
def selamlama():
    print("Merhaba")
    
selamlama() # Merhaba Merhaba

@fn_x2
def isimle(ad):
    print("Merhaba " + ad)

selamlama()
isimle("Berke") # TypeError: wrapper_fn_x2() takes 0 positional arguments but 1 was given
#o yuzden args ve kwargs kullanmamiz gerekiyor
#--------------------------------------------------------------------------------
#decorator args
def dec_fn_x2(count):
    def fn_x2(func):
        def wrapper_fn_x2(*args, **kwargs):
            for i in range(count):
                func(*args, **kwargs)
        return wrapper_fn_x2
    return fn_x2

@dec_fn_x2(count = 4)
def selamlama():
    print("Merhaba")

@dec_fn_x2(count = 2)
def isimle(ad):
    print("Merhaba " + ad)

selamlama() # Merhaba Merhaba Merhaba Merhaba
isimle("Berke") # Merhaba Berke Merhaba Berke