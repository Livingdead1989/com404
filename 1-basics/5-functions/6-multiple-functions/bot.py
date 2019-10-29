# First function
def display_ladder(steps):
    # initial print for ladder
    print("| |")
    # for loop to produce ladder steps
    for step in range(0, steps):
        print("***")
        print("| |")
          
# Second function
def create_ladder():
    steps = int(input("How many steps remain?\n"))
    print("\n")
    display_ladder(steps)
    
# Call function
create_ladder()
    