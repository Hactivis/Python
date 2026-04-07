#My Code
branch_a_products = {"bread", "milk", "butter", "jam"}
branch_b_products = {"bread", "cheese", "butter", "ketchup"}
print(f"{branch_a_products}" )
print(f"{branch_b_products} ")
union = branch_a_products | branch_b_products
print(f"{union}")
common_products = branch_a_products & branch_b_products
print(f"{common_products}")
only_in_branch_a_products = branch_a_products - branch_b_products
print(f"{only_in_branch_a_products}")

print(f"Is 'ketchup' is available in branch_a_products:{'ketchup' in branch_a_products}")

essential_items = frozenset(["milk","bread","ketchup"])
print(f"{essential_items}")


# udemy Code
branch_a_products = {"bread", "milk", "butter", "jam"}
branch_b_products = {"bread", "cheese", "butter", "ketchup"}
print(f"{branch_a_products}" )
print(f"{branch_b_products} ")
print(branch_a_products | branch_b_products) 
print( branch_a_products & branch_b_products)

print(branch_a_products - branch_b_products)  
print('ketchup' in branch_a_products)

essential_items = frozenset(["milk","bread","ketchup"])
print(essential_items)