first_number = int(input("Gimme a number: "))
print(first_number, "is a great number\n")

second_number = int(input("Now gimme another number: "))
print(second_number, "is another great number\n")

if (first_number > second_number):
    print(first_number, "is bigger")
elif (first_number < second_number):
    print(second_number, "is bigger")
elif (first_number == second_number):
    print("They have the same value")
else:
    print("ERROR")

print("Done")

