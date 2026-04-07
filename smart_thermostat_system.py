# device_status = "active"
# temperature = 38

# if device_status == "active":
#     if temperature > 35:
#         print("High temperature alert!")
#     else:
#         print("Temperature is normal")
# else:
#     print("Device is offline") 

    # This function will be tested by the evaluation system. Do not modify the function name or parameters.
age = 21
income = 25,000
def check_loan_eligibility(age: int, income: float) -> str:

    if age =< 21:
        if income =< 25,000:
            print("Eligible for Loan")
    else:
        print("Not eligible:income too low")