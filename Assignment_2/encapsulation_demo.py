class Student:
    def __init__(self, name, grade, roll_no, age):
        self.name = name
        self.age = age
        self.__grade = grade
        self.__roll_no = roll_no

    
    def get_roll_no(self):
        return self.__roll_no    # double underscore means private variable

    def get_grade(self):
        return self.__grade 

    def set_grade(self, new_grade):
        self.__grade = new_grade  
        
    def __str__(self):
        return f" Name: {self.name} \n Age: {self.age}\n Roll No: {self.__roll_no}\n Grade: {self.__grade}"
        

s1 = Student("Prashanth", "A", 25, 30)
print(s1.get_roll_no())  # Access private attribute through method
s1.set_grade("A+")
print(s1.get_grade())  # Updated grade