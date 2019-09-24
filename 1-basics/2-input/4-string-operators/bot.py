number_of_lives = int(input("Please enter the number of lives.\n"))
energy_level = int(input("Please enter the energy level.\n"))
shield_level = int(input("Please enter the shield level.\n"))

print("\nHealth has been set.\n")
print("Lives:", (number_of_lives * "❤"))
print("Energy:", (energy_level * "X"))
print("Shield:", (shield_level * "V"))