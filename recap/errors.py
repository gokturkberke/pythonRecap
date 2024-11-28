# This file is created to show how to handle errors in python

try:
    a = int(input("number 1 : "))
    b = int(input("number 2 : "))

    print(a+b)

except:
    print("Invalid input")
#----------------------------------------------
#syntax error(Yazim hatasi)
#print("berk"e) while True()): gibi hatalar

#type error
# len(10) , 10 + "a" gibi hatalar

#value error
#int("abc")  # Raises ValueError
#float("xyz")  # Raises ValueError
#range(1.5)  # Raises ValueError

#Error management
while True:
    try:
        a = int(input("number 1 : "))
        b = int(input("number 2 : "))

        print(a/b)
        
    #except (ZeroDivisionError, ValueError) as e:  seklinde ikisini de birlestirebiliriz ve aldigi hatayi print(e) yaparak kullanaciya gosterebiliriz

    except ZeroDivisionError:
        print("B number can not be zero")

    except ValueError:
        print("just enter number")

    except Exception:
        print("Unknown error")
    
    else:
        break
    finally: #bu kod her zaman calisir
        print("Finally block")
#mesela 
#finally:
     #dosya.close() dosya her durumda kapatilirdi
       
#Bilgiler dogru girene kadar calisir dogru girdiginde durur
#---------------------------------------------------
#Raise error

def users(username,city):
    citys = ["ankara", "istanbul", "izmir","antalya","bursa"]
    if type(username) != str: #is not str veya type(username) != str ayni sey
        raise TypeError("username must be string")
    if type(city) != str:
        raise TypeError("city must be string")
    if city not in citys:
        raise ValueError("city is not valid")

try:
    users("berke", "ankara")
except Exception as e:
    print(e)
else:
    print("user added")