def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
x = int(input("enter a number"))
print(is_even(x))

def bigger(r,m):
    if r>m :
        print(f"{r}")
    elif r==m:
        print("both are equal")
    else:
        print(f"{m}")
y = int(input("enter the first number"))
z = int(input("enter the second number"))
bigger(y,z)