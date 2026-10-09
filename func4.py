def greet(name,greet="hello"):
    return f"{greet} ! {name}"
v = input("enter your name ")
print (greet(v))
m=input("enter a greeting")
print( greet(v,m))
