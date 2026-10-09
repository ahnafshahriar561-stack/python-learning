def positive_sum(*args):
    total = 0
    for num in args:
        if num  > 0:
            total += num
    return total
m = positive_sum(45,-2,-77,8,12,3,444)
print(f"the summation is {m}")
