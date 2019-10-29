print("Welcome to the Planet of the Apes...")
humans = 0
apes = 0

for iteration in range(0,7):
    human_or_ape = input("be ye human or be ye ape? ")
    if(human_or_ape.lower() == "human"):
        humans = humans + 1
        print("I did not start this war. But i will finish it.")
    elif(human_or_ape.lower() == "ape"):
        apes = apes + 1
        print("Apes together strong!")
    else:
        print("This is not your fight.")
        
print("Total humans encountered:",humans)
print("Total apes encountered:",apes)
