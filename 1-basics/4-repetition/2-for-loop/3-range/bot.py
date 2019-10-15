night_vision = int(input("What level of brightness is required?"))
print("You have entered: " + str(night_vision) + "\n")

for count in range(2,night_vision + 1,2):
    print("Beep's brightness level:", ('*' * count))
    print("Bop's brightness level:", ('*' * count))
    print("\n")