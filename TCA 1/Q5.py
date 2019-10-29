health = 100
print("Your health is 100%. Escape is in progress...")
# loop which runs 5 times
for who in range(0,5):
    who_is_that = input("…Oh dear, who is that? ")
    print(who_is_that)
    # adjust health variable based on users input and print back to the user
    if(who_is_that == "Smiler's Bot"):
        health = health - 20
        print("Time to jam out of here!")
    elif(who_is_that == "Hacker"):
        health = health + 20
        print("Yay! Better follow this one!")
    else:
        print("Phew, just another emoji!")
        
print("Escaped! Health is", health)