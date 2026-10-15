
def min_max(a, b, c):
    smallest = a
    largest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    if largest < b:
        largest = b
    if largest < c:
        largest = c
    return smallest, largest

x = int(input("Enter 1st number: "))


y = int(input("Enter 2nd number: "))


z = int(input("Enter 3rd number: "))


lo, hi = min_max(x, y, z)
print(f"The largest is {hi} and the smallest is {lo}")