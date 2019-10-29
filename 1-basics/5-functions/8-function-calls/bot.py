# Display in a box function
def box(the_word):
    print("|", "-" * len(the_word), "|")
    print("|", the_word, "|")
    print("|", "-" * len(the_word), "|")
    
# Display lower case
def lower(the_word):
    print(the_word.lower())
    
# Display upper case
def upper(the_word):
    print(the_word.upper())
    
# Display inverted (mirror)
def mirror(the_word):
    reverse = ""
    for character in range((len(the_word)-1), -1, -1):
        reverse = reverse + the_word[character]
    print(the_word, "|", reverse)
    
# Display repeat (case change)
def repeat(the_word):
    repeat_number = int(input("How many times would you like to repeat?\n"))
    for interation in range(0, repeat_number):
        if(interation % 2):
            print(the_word.lower())
        else:
            print(the_word.upper())
    
# Run function
def run():
    action = input("""Choose an option:
(box, lower, upper, mirror, repeat) """)
    print("You have selected:",action, "\n")
    the_word = input("Enter your word: ")
    
    # if statements to control the action performed
    if(action == "box"):
        box(the_word)
    elif(action == "lower"):
        lower(the_word)
    elif(action == "upper"):
        upper(the_word)
    elif(action == "mirror"):
        mirror(the_word)
    elif(action == "repeat"):
        repeat(the_word)
    else:
        print("I didn't understand that.")
    
# Calling the run function
run()
