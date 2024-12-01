# with open("markalar.txt","a") as file:
#     file.write("7-Xiaomi\n")
    
    
# with open("markalar.txt","r") as file:
#     print(file.read())

with open("markalar.txt","r+") as file:
    markalar = file.read()
    markalar = "1-Samsung\n" + markalar
    file.seek(0) #imleci en basa goturduk yazdirmak icin
    file.write(markalar)
    
with open("markalar.txt","r") as file:
     print(file.read())
     

with open("markalar.txt","r+") as file:
    liste = file.readlines()
    liste.insert(2,"3-Nokia\n")
    file.seek(0)
    file.writelines(liste)
    
  #  for marka in markalar:
   #     file.write(marka) #1. yontem
   
   
        
with open("markalar.txt","r") as file:
     print(file.read())