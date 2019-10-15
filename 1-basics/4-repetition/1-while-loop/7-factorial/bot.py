number = 1
total = 1
max_number= int(input("Please enter a number: "))


while(number <= max_number):
    total = total * number
    number = number + 1
    print(total)
    
print("The factorial is", total)