from abc import ABC, abstractmethod

class Person(ABC):  # to enforce abstract class method rule in child class we must use ABC
    @abstractmethod
    def get_details(self):
        pass

class Student(Person):
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def get_details(self):
        return f"Student: {self.name}, Roll No: {self.roll_no}"
    
s1 = Student("Prashanth", 25)
print(s1.get_details())
