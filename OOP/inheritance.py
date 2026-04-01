# ke thua

class Person:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Name: {self.name}")
        
# class ke thua
class Student(Person):
    # tai su dung lai ham khoi tao cua lop cha
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

# tao doi tuong
student1 = Student("Alice", 10)
student1.display_info()  
print(student1.age)