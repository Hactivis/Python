masala_spices = ("cardamom", "cloves", "cinnamon", "ginger")

(spice1, spice2, spice3, spice4) = masala_spices

print(f"Main masala spices: {spice1},{spice2},{spice3}")

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ration of G:{ginger_ratio} and C:{cardamom_ratio}")

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratio of G:{ginger_ratio} and C:{cardamom_ratio}")

# membership

print(f"Is ginger in masala spices ? {'ginger' in masala_spices}")
print(f"Is ginger in masala spices ? {'cinnamon' in masala_spices}")