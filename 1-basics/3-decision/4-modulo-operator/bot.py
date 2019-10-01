# The program should start by prompting the user to enter a whole number.
# The program should then work out if the number is even or odd.
# Finally, the program should display a suitable message to indicate if the number is even or odd.

whole_number = int(input("Enter a whole number"))

if ( whole_number % 2):
    print("The number", whole_number, "is odd")
else:
    print("The number ", whole_number, "is even")

print("Done")