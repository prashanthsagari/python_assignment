class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no
    
    def get_student_info(self):
        return f"{self.get_info()}, Roll No: {self.roll_no}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def get_teacher_info(self):
        return f"{self.get_info()}, Subject: {self.subject}"

s1 = Student("Prashanth", 30, 25)
t1 = Teacher("Ganesh", 45, "Mathematics")

print(s1.get_student_info())  
print(t1.get_teacher_info())  