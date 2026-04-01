# da hinh

# class Cow:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return self.name + " says Moo!"

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return self.name + " says Meow!"
    
    
# my_cow = Cow("Bessie")
# my_cat = Cat("Whiskers")

# print(my_cow.speak())  # Output: Bessie says Moo!
# print(my_cat.speak())  # Output: Whiskers says Meow!


class Animal:
    def speak(self):
        return "sound"
# ke thua
class Cow(Animal):  # overriding method
    def speak(self):
        return " says Moo!"
    
my_cow = Cow()
my_cat = Animal()
print(my_cow.speak())  # Output: Bessie says Moo!
print(my_cat.speak())  