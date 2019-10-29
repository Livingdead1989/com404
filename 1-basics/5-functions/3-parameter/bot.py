def escape_by(plan):
    if(plan == "jumping over"):
        print("We cannot escape that way!\n The boulder is too big!\n")
    elif(plan == "running around"):
        print("We cannot escape that way!\n The boulder is to fast!\n")
    elif(plan == "going deeper"):
        print("That might just work!\n Lets go deeper!\n")
    else:
        print("We cannot escape that way!\n The boulder is in the way!\n")
        
# Calling the function with different perameters
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
escape_by("gas powered roller blades")

    