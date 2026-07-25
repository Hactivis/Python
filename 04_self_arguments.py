# class Marvel:
#     SuperHero = "IronMan"
#     SuperHero2 = "Spiderman"
#     SuperHero3 = "Captain America"
#     SuperHero4 = "Thor"
#     SuperHero5 = "Hulk"

#     def name(self):
#         return f"SuperHero {self.SuperHero2} is a amazing hero"

# Hero = Marvel()
# print(Hero.name())

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(self.name)
#         print(self.age)

# s1 = Student("Rishabh", 20)
# s1.display()

# Accessing another Method

class Student:
    def greet(self):
        print("hello")

    def display(self):
        self.greet() # calling another method using self 

s = Student()
s.display()