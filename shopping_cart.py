food =[]
price = []
total = 0
while True:
    x = input("enter a food you want to buy(press r to exit)")
    if x =='r' or x=='R':
        break
    else:
        y = int(input("enter the price of the food"))
        food.append(x)
        price.append(y)

print(food)
print(price)
i = len(food)
for x in range(0,i):
    total = int(total + price[x])
print(f"there are {i} number of food and total price is {total}")
