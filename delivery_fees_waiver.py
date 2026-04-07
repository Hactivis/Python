# order_amount = int(input("Enter the order amount: "))

# delivery_fees = 0 if order_amount > 300 else 30

# print(f"Delivery fees is : {delivery_fees}")

def verify_age(age_str: str) -> str:
    age = int(age_str)
    return "Access Granted" if age >= 18 else "Access Denied"
    pass