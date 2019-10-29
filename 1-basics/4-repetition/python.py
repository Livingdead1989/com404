### SIMPLE FOR LOOPS
## Activity 3: Range
# brightness = int(input("What level of brightness is required? "))
# print("You have selected:", brightness)
# for x in range(2, brightness, 2):
#     print("Beep's brightness level: ", ("*" * x))
#     print("Bop's brightness level:  ", ("*" * x))
#     print("\n")

## Activity 4: Characters
# markings = input("What strange markings do you see? ")
# print("You saw the following markings:", markings, "\n")
# for m in range(0, len(markings), 1):
#     print("index " + str(m) + ":", markings[m])

## Activity 5: Reverse Word
# phrase = input("What phrase do you see? ")
# reverse = ""
# print("You saw the phrase:", phrase, "\n")
# print("Reversing...\n")
# for p in range((len(phrase)-1), -1, -1):
#     reverse = reverse + phrase[p]
# print("The phrase is:", reverse)


### NESTED LOOPS
## Activity 1: Nested Loop
# rows = int(input("How many rows should I have?\n"))
# columns = int(input("How many columns should I have?\n"))
# print("Here I go:")
# for r in range(0, rows, 1):
#     for c in range(0, columns,1):
#         print(":) ", end="")
#     print("\n")
# print("Done!")

## Activity 2: Nestings
sequence = input("Please enter a sequence consisting of dashes and two markers\n")
marker = input("Please enter the character for the marker e.g. 'x'\n")
print("\n")
position_counter = 0
first_marker = 0
last_marker = 0
for mark in (sequence):
    position_counter += 1
    # if the character matches
    if(mark == marker):
        # if first_marker has a value
        if(first_marker > 0):
            last_marker = position_counter
        # else set first_marker
        else:
            first_marker = position_counter
print("The distance between the markers is:", (last_marker - first_marker -1))

# find the first marker, store position
# find the second marker, store position
# calculate the difference between the two