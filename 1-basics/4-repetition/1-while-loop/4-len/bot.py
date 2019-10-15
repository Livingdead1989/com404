bop_counter = 0
users_phrase = input("Please enter a phrase: ")
print("Your phrase is", users_phrase, "which is", len(users_phrase), "characters long\n")

while( bop_counter < len(users_phrase) ):
    print("Bop ", end="")
    bop_counter = bop_counter + 1