# class Students:
#     def __init__(self,name):
#         self.name = name

# s1 = Students("Alice")
# s2 = Students("bob")

# print(s1.name)
# print(s2.name)

# class Students:
#     def __init__(self,name):
#         self.name = name

#     def introduce(self):
#         print("Hi, I am", self.name)

# s = Students("Tony")
# s.introduce()


# numbers = [10, 20, 30, 40]
# print(numbers[0])

# numbers.append(50)

# numbers.remove(20)

# print(numbers)

# coordinates = (10, 20)
# print(coordinates[0])

# stduents = {
#     "name": "john",
#     "age": 29,
#     "marks":91
# }

# print(stduents["name"])
# print(stduents["age"])
# print(stduents["marks"])

# def square(X):
#     return X * X

# print(square(5))

# squares = [i*i for i in range(10)]
# print(squares)

# reviews = {
#     "Good",
#     "Bad",
#     "Excellent"
# }

# for review in reviews:
#     print(review.lower())


# file = open("notes.txt", "r")
# print(file.read())
# file.close

# with open("notes.txt", "r") as file:
#     print(file.read())

with open("notes.txt", "w") as file:
        file.write("Python is Easy")
        file.write("Welcome to AI")