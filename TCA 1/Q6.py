def is_league_united(first_hero, second_hero):
    # test if the hero variables equal either key heros using OR and AND
    if(first_hero.lower() == "superman" and second_hero.lower() == "wonder woman" or first_hero.lower() == "wonder woman" and second_hero.lower() == "superman"):
        return True
    else:
        return False
  
def decide_plan(first_hero, second_hero):
    # check if the league is united
    is_league_united(first_hero, second_hero)
    # decises an action based on if the league is united 
    if(is_league_united(first_hero, second_hero) == True):
        print("Time to save the world!")
    else:
        print("We must unite the league!")
        
def run():
    first_hero = input("Enter the name of the first hero ")
    second_hero = input("Enter the name of the second hero ")
    action = input("league or plan? ")
    # decise action based on user inputs
    if(action == "league"):
        print(is_league_united(first_hero, second_hero))
    elif(action == "plan"):
        decide_plan(first_hero, second_hero)
    else:
        print("Invalid command. Please try again")

# Run the program
run()
        