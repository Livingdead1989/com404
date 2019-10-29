# define function
def cross_bridge(steps):
    for step in range(0,steps,1):
        print("Crossed step.")
    if(steps > 5):
        print("The bridge is collapsing!\n")
    else:
        print("We must keep going!\n")

# Call function
cross_bridge(3)
cross_bridge(6)