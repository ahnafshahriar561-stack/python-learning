

bal =0

def balance():

    return f"the balance is {bal}"
def deposit(m):
    global bal
    bal =bal +m
    return bal
def withdraw(k):
    global bal
    if k>bal :
        print("you can not withdraw more than you have in account")

        return  False
    else:
        bal =  bal - k
        print("successfully withdraw")
        return bal
def main():

    global bal
    bal = int(input("enter your previous balance"))

    while True:
        d = int(input("what you want to do\n 1 show balance\n 2 deposit money \n 3 withdraw money \n 4 exit"))

        if d == 1:
            print(balance())

        elif d == 2:
            r = int(input("enter how much you want to deposit   "))

            print("sucessfully deposited")
            print(f"after deposit {deposit(r)}")

        elif d== 3:
            r = int(input("how much you want to withdraw "))


            print(f"after withdraw {withdraw(r)}")

        elif d==4:
            break
        else:
            print("out of the board")
if __name__ == '__main__':                   # CHANGE 5
    main()