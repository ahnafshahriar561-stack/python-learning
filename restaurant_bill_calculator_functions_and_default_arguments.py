def bill_calculator(amount,discount=0,tax =5):
    discounted = amount*(1-(discount/100))
    return (discounted*(1+(tax/100)))

a = int(input("enter the amount of food bill"))
bill= bill_calculator(a)
print(f"the final bill is {bill}")