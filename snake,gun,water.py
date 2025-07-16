import random

# 1 = snake, -1 = water, 0 = gun
computer = random.choice([-1, 1, 0])

# dictstr = {"s": 1, "w": -1, "g": 0}

you = int (input("enter your choice(1 for snake , -1 for water , 0 for gun )"))
reversedict = {1: "snake", -1: "water", 0: "gun"}
print(f"Your choice: {reversedict[you]}")
print(f"Computer's choice: {reversedict[computer]}")

if(computer == you):
        print("Match is tie !!")
else:
        if(computer== 1 and you == -1):
            print("You lost!!")
        elif(computer == 1 and you == 0):
            print("You win!!")
        elif(computer == -1 and you == 1):
            print("You win!!")
        elif(computer == -1 and you == 0):
            print("You lost!!")
        elif(computer == 0 and you == -1):
            print("You win!!")
        elif(computer == 0 and you == 1):
            print("You lost!!")
        else:
            print("Something went wrong!!")
