# collect a word from the user
the_word = str(input("Enter a word: "))

# print a menu of available options and prompt user for their selection
print("""
Enter the number for the action you wish to perform
1. Under
2. Over
3. Both
4. Grid
""")
option = int(input("Option ID: "))
    
# function which performs the action selected by the user
def actions(option, the_word):
    # action for under
    if(option == 1):
        print(the_word)
        print("*" * len(the_word))
        
    # action for over
    elif(option == 2):
        print("*" * len(the_word))
        print(the_word)
        
    # action for both    
    elif(option == 3):
        print("*" * len(the_word))
        print(the_word)
        print("*" * len(the_word))
        
    # action for grid    
    elif(option == 4):
        rows = int(input("Number of rows: "))
        columns = int(input("Number of columns: "))
        print("\n")
        
        # series of for loops to create the rows and columns based on the users input
        for row in range(0, rows):
            # top border row
            print("  ", end="")
            for column in range(0, columns):
                print("*" * len(the_word) + "   ", end="")
            print("\n")
            
            # middle text row
            print("| ", end="")
            for column in range(0, columns):
                print(the_word + " | ", end="")
            print("\n")
        
        # bottom border row
        print("  ", end="")
        for column in range(0, columns):
                print("*" * len(the_word) + "   ", end="")
    
    else:
        print("Error")

# run the actions function
actions(option, the_word)
        
