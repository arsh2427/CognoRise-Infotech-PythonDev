import random

# get the number of sides for the dice
num_sides = int(input("How many sides does the dice have? "))

# roll the dice
roll_again = "y"
while roll_again == "y":
    print("Rolling the dice...")
    print("The result is:", random.randint(1, num_sides))
    roll_again = input("Roll again? (y/n) ").lower()