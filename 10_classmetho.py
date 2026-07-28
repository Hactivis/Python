# class Student:
#         school = "ABC school"
#
#         @classmethod
#         def get_school(cls):
#                 return cls.school
#
# print(Student.get_school())
#
# class Student:
#         school = "ABC school"
#
#         @classmethod
#         def change_school(cls, new_name):
#                 cls.school = new_name
#
# Student.change_school("XYZ school")
# print(Student.school)

class BankAccount:
        def __init__(self, owner, balance):
                self.owner = owner
                self.balance = balance

        def deposit(self, amount):
                self.balance += amount

account = BankAccount("Rishabh", 1000000)
account.deposit(500)

print(account.balance)