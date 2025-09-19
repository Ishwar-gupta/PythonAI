"""
1 for snake
-1 for water
0 for gun
"""

import random

# Generating random number between -1 to 1
computer=random.choice([-1,0,1])
yourstr=input("Enter your choice:")
youDict={
    "s":1,
    "w":-1,
    "g":0
}
reverseDict={
    1:"Snake",
    -1:"Water",
    0:"Gun"
}
you=youDict[yourstr]
print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")
else:
    if(computer - you)==-2 or (computer -you)== 1 :
        print("You Win !!")
    elif((computer - you)==-1 or (computer-you)==2):
        print("You lose")
    else:
        print("oops! Something went wrong")

    # if(computer == -1 and you == 1):# -2
    #     print("You Win!!")
    # elif(computer == -1 and you ==0):# -1
    #     print("You Lose!!")
    # elif(computer == 1 and you ==-1):# 2
    #     print("You Lose!!")
    # elif(computer == 1 and you==0):# 1
    #     print("You Win!!")
    # elif(computer==0 and you ==-1):# 1
    #     print("You Win!!")
    # elif(computer ==0 and you ==1):# -1
    #     print("You Lose!!")
    # else:
    #     print("Something went wrong !!")
    