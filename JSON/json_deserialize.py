#terminalde cd JSON ve python3 json_deserialize.py yazdığımızda calisir
#deserialize(decode) : JSON formatındaki veriyi python veri tipine çevirme işlemidir.
import json


with open("user.json") as file:
    data = json.load(file)
    print(data)
    print(type(data)) #<class 'dict'>
    print(data["userName"]) #BerkeKorkut
    print(data["age"]) #20

#json-string

data = """
{
    "usernName": "BerkeKorkut",
    "firstName": "Berke",
    "lastName": "Korkut",
    "email": "gokturkberke1907@gmail.com",
    "hobbies": ["Programming", "Playing Guitar", "Playing Games"],
    "age": 21,
    "isStudent": true
}
"""
data = json.loads(data)

print(data)
print(type(data)) #<class 'dict'>
