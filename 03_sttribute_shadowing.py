class Ironman:
    Power = "Billinior"
    strength = "Knowlege"

marvel = Ironman()
print(marvel.Power)

marvel.Power = "Mark 32 Suit"
print("After Changing", marvel.Power)
print("Direct look into class", Ironman.Power)

del marvel.Power
print(marvel.Power)