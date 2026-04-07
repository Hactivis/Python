my_cart = ["apple", "bananas", "milk"]
print(f"my cart:{my_cart}")
my_cart.append("bread")
print(f"updated grocery list:{my_cart}")
my_cart.insert(0, "ketchup")
print(f"{my_cart}")
my_cart.remove("bananas")
print(f"{my_cart}")
last_added = my_cart.pop()
removed_item = ["bread"]
print(f"{last_added}")
print(f"{removed_item}")
my_cart.append("rice")
my_cart.append("butter")
print(f"{my_cart}")
my_cart.sort()
print(f"{my_cart}")
my_cart.reverse()
print(f"{my_cart}")
juice = ["mango", "apple", "banana","blueberry"]
jam = ["mango jam", "blueberry jam",]
my_cart.extend(juice)
my_cart.extend(jam)
print(f"{my_cart}")
my_cart.extend(my_cart)
print(f"{my_cart}")
vegetable = "tomato cucumber spinach"
vegetable_list = vegetable.split()
print(f"{vegetable_list}")