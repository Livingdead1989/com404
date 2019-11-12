# Creating the class
class Bot:   
    # Constructor Init
    # anything following a default value should have a default value
    def __init__(self, name, age=0):      
        self.name = name
        self.age = age
        self.energy = 10
        self.shield = 10

    def display_name(self):
        print("-" * (len(self.name) + 4))
        print("| {} |".format(self.name))
        print("-" * (len(self.name) + 4))

    def display_age(self):
        print("*" * (len( str(self.age) ) + 4) )
        print("|" * (len( str(self.age) ) + 4) )
        print("-" * (len( str(self.age) ) + 4) )
        print("| {} |".format(self.age))
        print("-" * (len( str(self.age) ) + 4) )
        
    def display_energy(self):
        print("Energy:", "X" * self.energy)
        
    def display_shield(self):
        print("Shield:", "O" * self.shield)
        
    def display_summary(self):
        print("My name is", self.name)
        print("I am", self.age)
        print("My current energy level is", self.energy)
        print("My shields are at", self.shield)
        

my_bot = Bot("William", 7)
#my_bot.display_name()
#my_bot.display_age()
#my_bot.display_energy()
#my_bot.display_shield()
my_bot.display_summary()

        
        
