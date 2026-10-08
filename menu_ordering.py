#vending machine ar moto item ar price ar dictionary toiri korbo...
price1=0
vending = {"mojo":"25","coca-cola":"25","energyplus":"15","potato-crackers":"20","milk-vita":"50","arong-labang":"40"}
for key,value in vending.items():
    print(f"{key:20}:{value}")
print("--------------------------")
while True:

    x=input("which item you want to buy(q to quit)")
    if x=='q':
        break
    else:
        amount =int(input("the amount you want to buy"))
        y = vending.get(x)
        price1 = price1 + amount*int(y)
print(f"your total cost is {price1}")