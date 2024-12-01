import json


user = {
    "usernName": "BerkeKorkut",
    "firstName": "Berke",
    "lastName": "Korkut",
    "email": "gokturkberke1907@gmail.com",
    "hobbies": ["Programming", "Playing Guitar", "Playing Games"],
    "age": 21,
    "isStudent": True
}

result = json.dumps(user,ensure_ascii=False,indent=2) # Serialize sozluk veri tipini stringe donusturur dumps
#ensure ascii turkce karakterler icin False yapilir eger varsa
print(type(result)) # <class 'str'>

with open("user.json","w") as file:
    json.dump(user,file,ensure_ascii=False,indent=2) # Serialize sozluk veri tipini json dosyasina yazar
    #indent 2 de ikili ikili yazmasini saglar kodun
    #yani userName = ... alta satira gecer age = 20

