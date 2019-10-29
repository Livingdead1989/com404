# importing other python script but only the actions function
import functions
from functions import actions

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
    

# run the actions function
functions.actions(option, the_word)
        
