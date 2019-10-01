# Nested IF statements
book_type = input("What type of cover does the book have?")

if ( book_type == "soft" ):
    book_binding = input("Is the book perfect-bound?")
    if ( book_binding == "yes" ):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books.")
        
elif ( book_type == "hard" ):
    print("Books with hard covers can be more expensive!")
    
else:
    print("Your book is out of this world!")