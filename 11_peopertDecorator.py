# class Student:
#     def __init__(self, marks):
#         self.marks = marks
#
#     def get_grade(self):
#         if self.marks >= 90:
#             return "A"
#         elif self.marks >= 75:
#             return "B"
#         else:
#             return "C"
#
# s = Student(92)
# print(s.get_grade())

# class Rectangle:
#     def __init__(self, height, weight):
#         self.height = height
#         self.weight = weight
#
#     def get_area(self):
#         return self.height * self.weight
#
# r = Rectangle(10 , 5)
# print(r.get_area())
#
# class Rectangle:
#     def __init__(self, height, weight):
#         self.height = height
#         self.weight = weight
#
#     @property
#     def area(self):
#        return self.height * self.weight
#
# r = Rectangle(5 , 3)
# print(r.area)
#
########## without Validation ###############
#
# class Student:
#     def __init__(self):
#         self.marks = 0
#
# s = Student()
# s.marks = -50
# print(s.marks)


########## With Validation ##################
#
# class Student:
#     def __init__(self):
#         self._marks = 0
#
#     @property
#     def marks(self):
#         return self._marks
#
#     @marks.setter
#     def marks(self, value):
#         if value < 0:
#             raise ValueError("marks cannot be Negative")
#
#         self._marks = value
#
# s = Student()
# s.marks = 95
# print(s.marks)


################################################### IMPORTANT ######################################################
class User:
    def __init__(self):
        self._password = ""

    @property
    def password(self):
        return "**********"

    @password.setter
    def password(self, value):
        # Validation or hash the password here
        self._password = value