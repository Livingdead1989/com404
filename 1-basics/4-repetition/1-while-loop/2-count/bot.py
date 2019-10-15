cable_counter = 0
live_cables = int(input("How many live cables should I avoid?: "))
print("I will avoid", live_cables, "live cables.\n")

while ( cable_counter < live_cables):
    cable_counter = cable_counter + 1
    print("Avoiding...Done!", cable_counter, "live cables avoided.")
    
    
print("\nAll live cables have been avoided.")