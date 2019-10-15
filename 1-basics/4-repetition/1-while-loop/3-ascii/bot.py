# counter variable set to 0 on start
charging_counter = 0
charge_bars = int(input("How many bars should be charged?: "))

while( charging_counter < charge_bars ):
    # counter variable incrementing each loop
    charging_counter = charging_counter + 1
    # variable to stack the bars
    charged_bars = "x" * charging_counter
    
    print("Charging:", charged_bars)

print("\nThe battery is fully charged.")