counter = 0
total_numbers = int(input("How many numbers should I sum up?: "))
print("You entered", total_numbers)

while(counter < total_numbers):
    new_number = int(input("Another number: "))
    counter = counter + 1
    #calc
    grand_total = new_number + new_number
                     
                     
print("The answer is", grand_total)