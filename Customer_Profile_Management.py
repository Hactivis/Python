customer = {"name":"John Doe","age":32, "city":"New York"}
print(f"{customer}")

update_customer = {"email": "", "phone": ""}
customer.update(update_customer)


# print(f"{customer.values()}")
print(customer.pop("age"))
print(customer.keys())
print(customer.values())
print(customer.items())

removed_last_inserted = customer.popitem()
print({removed_last_inserted})

customer.update ({"address": "221B Baker Street"})
print(customer)

