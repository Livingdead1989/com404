print("What is your name human?")
name = input()

print("How old are you (in years)?")
age = int(input())

print("How tall are you (in meters)?")
height = float(input())

print("How much do you weigh (in kilograms)?")
weight = float(input())

# Variable to calc bmi and converted to a int
bmi = int(weight / height * height)

# Print statement with varaibles
print(name, "you are", age, "years old and your bmi is", bmi)