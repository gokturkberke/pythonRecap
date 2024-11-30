#encapsulation
def dis_fonksiyon(sayi1):
    print("dis_fonksiyon calisti")
    def ic_fonksiyon(sayi2):
        print("ic_fonksiyon calisti")
        return sayi1 **2
    sayi2 = ic_fonksiyon(sayi1)
    print(sayi1,sayi2)
    
#dis_fonksiyon(5) #dis_fonksiyon calisti
#ic_fonksiyon(5) #NameError: name 'ic_fonksiyon' is not defined
#cagirmamiz lazim sayi2 = ic_fonksiyon(sayi1)
dis_fonksiyon(5) #5 25
#-----------------------------------------------------

def faktoriyel(number):
    if not isinstance(number,int): #eger number int degilse demek bu kod
        raise TypeError("Please enter a valid number")
    if not number >= 0:
        raise ValueError("Please enter a positive number")
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number-1)
    return inner_factorial(number)
#print(faktoriyel(5)) #120
#print(faktoriyel("5")) #TypeError: Please enter a valid number
#print(faktoriyel(-5)) #ValueError: Please enter a positive number