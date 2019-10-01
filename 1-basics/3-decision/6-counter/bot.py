# Beep wishes to count up the number of even and odd numbers.
odd_numbers = 0
even_numbers = 0


first_number = int(input("First Number: "))

if ( first_number % 2 ):
    print("first number is odd")
    odd_numbers = odd_numbers + 1
elif ( 1 % first_number ):
    print("first number is even")
    even_numbers = even_numbers + 1
else:
    print("ERROR")

second_number = int(input("Second Number: "))

if ( second_number % 2 ):
    print("second number is odd")
    odd_numbers = odd_numbers + 1
elif ( 1 % second_number ):
    print("second number is even")
    even_numbers = even_numbers + 1
else:
    print("ERROR")
                   
third_number = int(input("Third Number: "))

if ( third_number % 2 ):
    print("third number is odd")
    odd_numbers = odd_numbers + 1
elif ( 1 % third_number ):
    print("third number is even")
    even_numbers = even_numbers + 1
else:
    print("ERROR")
    
print("You gave me", even_numbers, "even numbers and", odd_numbers, "odd numbers.")
                   
