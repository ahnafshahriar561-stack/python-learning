#aikhane random number toiri korbo ar user ke oita guess korte hobe. jotogula guess lagbe ta gunbo
import random
from curses.ascii import isdigit

lowest_num = 1
highest_num = 50
answer=random.randint(lowest_num,highest_num)
guess= 0
is_true = True
while is_true:
    x = int(input(f"enter you guess(it should be between {lowest_num} to {highest_num}"))
    if x == answer:
        is_true=False
    elif x>highest_num or x<lowest_num  :
        print(f"invalid guess ... it must be between {lowest_num} and {highest_num}")
    elif x>answer:
        print("too high")
        guess += 1
    else :
        print("too low")
        guess += 1


guess = guess +1
print(f"the number of guess needed  {guess}")
