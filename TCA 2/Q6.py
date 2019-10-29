def isFusionShot(slug1, slug2):
    if(slug1 == slug2):
        return True
    else:
        return False

def isDefectiveShot(slug1, slug2):
    fusion = isFusionShot(slug1, slug2)
    if(fusion == False):
        return True
    else:
        return False

def run():
    slug1 = input("Enter first slug (Infurnus/AquaBeek) ")
    slug2 = input("Enter second slug (Infurnus/AquaBeek) ")
    action = input("Fusion or Defective? ")
    
    print("\n")
    
    if(action.lower() == "fusion"):
        print(isFusionShot(slug1, slug2))
    elif(action.lower() == "defective"):
        print(isDefectiveShot(slug1, slug2))
    else:
        print("Invalid selection. Please try again")

run()

        
    
