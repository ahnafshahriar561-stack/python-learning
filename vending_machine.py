#vending machine ar moto item ar price ar dictionary toiri korbo...
vending = {"mojo":"25tk","coca-cola":"25tk","energyplus":"15tk","potato-crackers":"20tk","milk-vita":"50tk","arong-labang":"40tk"}
for key,value in vending.items():
    print(f"{key:20}:{value}")
print("--------------------------")
x=input("which item you want to buy")
