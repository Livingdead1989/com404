import function

given_number = int(input("Enter a 5 digit number: "))

print("You entered:", given_number, """
1. Display ASCII Triangle
2. Display Left Digits Triangle
3. Display Right Digits Triangle
""")

selected_option = int(input("Enter your selection ID: "))

function.actions(selected_option, given_number)
