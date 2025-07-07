ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai:{chai_ingredients}")
last_added = chai_ingredients.pop()
print(f"{last_added}")
first_added = chai_ingredients.pop()
print(f"{first_added}")