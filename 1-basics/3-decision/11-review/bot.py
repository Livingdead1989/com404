# What Type of Device
device_type = input("What type of device do you have? ")

if(device_type == 'router'):
    print("You have a router\n")
    router_model = input("What is the model? ")
    
    if ( (router_model == 'cisco') or (router_model == 'hpe') or (router_model == 'netgear') ):
        print("You have a enterprise grade router\n")
    else:
        print("You have a consumer product")
        
elif(device_type == 'switch'):
    print("You have a switch\n")
else:
    print("You have something unknown to me")
    