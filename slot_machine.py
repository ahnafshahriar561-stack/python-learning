import random
def spining():

    options = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    x1 = random.choice(options)
    x2 = random.choice(options)
    x3 = random.choice(options)

    return [x1 , x2 ,x3]
def is_win(row):
    return row[0] == row[1] == row[2]
def main():
    balance = int(input("enter the balance for entire session"))
    while True:

        run = int(input("1 for bet \n 2 for quit"))
        if run ==1:

            bet = int(input("enter the bet amount"))
            if bet > balance:
                print("you can not bet more than your balance")
            else:
                row = spining()
                print(row)
                if is_win(row):
                    print("you win")
                    balance +=(bet*5)
                else:
                    print("you lose")
                    balance = balance-bet
        if run ==2:
            print(f"your final balance is {balance}")
            break

if __name__=='__main__':
    main()