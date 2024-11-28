#Inheritance

class Person:
    def __init__(self, name, age,surname):
        print("Person created")
        self.name = name
        self.age = age
        self.surname = surname
    
    def info(self):
        return f"{self.name} {self.surname} is {self.age} years old"

class Student(Person):
    def __init__(self, name, age, student_id,surname):
        print("Student created")
        super().__init__(name, age,surname)
        self.student_id = student_id
        
    def ortalama_al(self):
        print(f"{self.student_id} numarali ogrencinin ortalamasi alindi")
        

class Teacher(Person):
    def __init__(self, name, age, branch,surname):
        print("Teacher created")
        super().__init__(name, age,surname)
        self.branch = branch
        
p1= Person("John", 36,"Doe")
p1.info()
s1 = Student("Jane", 23, "123","Doe")
s1.info()
t1 = Teacher("Tom", 45, "Mathematics","Doe")
t1.info()
