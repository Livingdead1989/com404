where_look = input("Where should I look? ")

if(where_look == 'in the bedroom'):
    place_look = input("Where in the bedroom should I look? ")
    if(place_look == 'under the bed'):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")
        
elif(where_look == 'in the bathroom'):
    place_look = input("Where in the bathroom should I look? ")
    if(place_look == 'in the bathtub'):
        print("Found a rubber duck but no battery")
    else:
        print("It is wet but I found no battery.")
        
elif(where_look == 'in the lab'):
    place_look = input("Where in the lab should I look? ")
    if(place_look == 'on the table'):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")
        
else:
    print("I do not know where that is but I will keep looking.")
