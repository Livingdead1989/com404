# Define function
def identify():
    object = input("What do you see? ")
    print("You saw", object)
    if(object == "a large boulder"):
        print("Its time to run!")
    else:
        print("We will be fine")

# Calling function
identify()