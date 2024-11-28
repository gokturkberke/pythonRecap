class User:
    def __init__(self, username, name,surname,birthday):
        self.username = username
        self.name = name
        self.surname = surname
        self.birthday = birthday
    #instance methods
    def info(self):
        return f"{self.name} {self.surname} was born in {self.birthday} with username {self.username}"
    
    def age(self):
        return 2024 - self.birthday
u1=User("Revenger","Berke","Korkut",2003)
u2=User("rvnger","Aziz","Korkut",2000)
print(u1.info()) # Berke Korkut was born in 2003 with username Revenger
print(u2.age()) # 24
#--------------------------------------------------------------
#Class Attributes
class User:
    active_users = 0
    
    def __init__(self, username, name,surname,age):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        User.active_users += 1
        
    def userName(self):
        return f"Username: {self.username}"
    def logout(self):
        User.active_users -= 1
        return f"{self.username} is logged out"

print(User.active_users) # 0
user1=User("revenger","Berke","Korkut",21)
user2=User("rvnger","Aziz","Korkut",24)
user3=User("berke_korkut","Gokturk","Korkut",27)
print(user2.logout())
print(User.active_users) # 2
#--------------------------------------------------------------
#Class Methods
class User:
    active_users = 0
    
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"
    #cls sınıfın kendisini temsil eder ve sınıf metodları içinde sınıf değişkenlerine ve diğer sınıf metodlarına erişmek için kullanılı
    @classmethod
    def from_string(cls,data_str):
        username, name, surname, age = data_str.split(",") #data_str = "GokceKorkut,Gokce,Korkut,25"
        return cls(username, name, surname, int(age))
        
    
    def __init__(self, username, name,surname,age):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        User.active_users += 1
        
    def userName(self):
        return f"Username: {self.username}"
    def logout(self):
        User.active_users -= 1
        return f"{self.username} is logged out"

print(User.display_active_users()) # 0
# user1=User("revenger","Berke","Korkut",21)
# user2=User("rvnger","Aziz","Korkut",24)
# user3=User("berke_korkut","Gokturk","Korkut",27)

user4=User.from_string("GokceKorkut,Gokce,Korkut,25")
print(User.display_active_users()) # 1