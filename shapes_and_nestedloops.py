rows = int(input("enter the number of rows"))
column = int(input("enter the number of column"))
symbol = input("enter the symbol you want to use")
for x in range(rows):
    for y in range(column):
        print(symbol,end="")

    print()