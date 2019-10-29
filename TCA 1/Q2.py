# ask the user to input
have_fear = str(input("Have you fear in your heart? "))
print(have_fear)
# lowers and compares users input against a string value
if(have_fear.lower() == "yes"):
    print("Fear is the path to the dark side. You cannot be a Jedi apprentice.")
else:
    print("The force is strong in you. You may be a Jedi apprentice.")