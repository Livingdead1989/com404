def actions(selected_option, given_number):
    if(selected_option == 1):
        print("Display ASCII Triangle\n")

        for iteration in range(0, 9):
            print("*" * iteration)
        print("*", given_number, "*")
        print("*" * 10)

    elif(selected_option == 2):
        print("Display Left Digits Triangle\n")
        numbers = ""

        for number in str(given_number):
            numbers = numbers + number
            print(numbers)
            
    elif(selected_option == 3):
        print("Display Right Digits Triangle\n")

        numbers = ""

        for number in str(given_number):
            numbers = numbers + number
            print(numbers.rjust(5))

    else:
        print("error - oops")
