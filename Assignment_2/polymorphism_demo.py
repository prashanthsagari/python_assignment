class Person:
    def role(self):
        return f"I am Person"
class Student(Person):
    
    def role(self):
        return f"I am Student"

class Teacher(Person):
    def role(self):
        return f"I am Teacher"
    
def print_role(person):
    print(person.role())
    
s1 = Student()
t1 = Teacher()

print_role(s1)
print_role(t1) 
