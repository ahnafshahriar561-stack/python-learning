#aitay random module use kore rock paper scissors kora hobe
import random


playerpoint=0
botpoint=0

r = int(input("how many round you want to play"))
for n in range(r):
    Player = input("enter your input(Rock,Paper,Scissors")
    options = ("Rock", "Paper", "Scissors")
    x = random.choice(options)
    if Player =='Rock' and x== 'Scissors':
        print("player win ")
        playerpoint +=1
    elif Player =='Scissors' and x== 'Paper':
        print("player win ")
        playerpoint +=1
    elif Player =='Paper' and x== 'Rock':
        print("player win ")
        playerpoint +=1
    elif (Player =='Paper' and x== 'Paper')  or (Player =='Scissors' and x== 'Scissors')  or (Player =='Rock' and x== 'Rock' ):
        print("tie")

    else:
        print("bot win")
        botpoint +=1
print(f"the player has {playerpoint} and the bot has {botpoint}")
if playerpoint>botpoint:
    print("---------Congratulations ------------")
    print("you won")
elif playerpoint==botpoint:
    print("Draw")
else:
    print("you lose")
    print("better luck next time")
