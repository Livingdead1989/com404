# first function
def sum_weights(bop_weight, beep_weight):
    total_weight = bop_weight + beep_weight
    return total_weight

# second function
def calc_avg_weight(bop_weight, beep_weight):
    avg_weight = sum_weights(bop_weight, beep_weight) / 2
    return avg_weight

# third function
def run():
    bop_weight = float(input("What is the weight of Bop?: \n"))
    beep_weight = float(input("What is the weight of Beep?: \n"))
    action = input("What do you want to do? (sum/average): \n")
    if(action == "sum"):
        print("The sum of Bop and Beep is", sum_weights(bop_weight, beep_weight))
    elif(action == "average"):
        print("The avgerage of Bop and Beep is", calc_avg_weight(bop_weight, beep_weight))
    else:
        print("I didn't understand that")
# calling
run()