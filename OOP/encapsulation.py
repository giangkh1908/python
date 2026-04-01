# dong goi

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # tao doi tuong
# my_stu = Student("John", 20)

# print("truoc khi thay doi", my_stu.name)  # John

# my_stu.name = "Jane"
# print("sau khi thay doi", my_stu.name)  # Jane


# Su dung dau gach duoi de dong goi thuoc tinh
class Student:
    def __init__(self, name): 
        self.__name = name


# tao doi tuong
my_stu = Student("John")

print("truoc khi thay doi", my_stu._Student__name)  # John

# my_stu._name = "Jane"
# print("sau khi thay doi", my_stu._name)  # Jane