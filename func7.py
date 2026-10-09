def total_num(*args):
    total =0
    for num in args:
        total +=num

    return total
def average_num(*args):
    count=0
    for num in args:
        count +=1
    if count ==0:
        print("you have not enter any input")
        return None
    return total_num(*args)/count
print(total_num(4,52,3,23,4,34,2,34,32,41,2,3,))
print(average_num(8,8,34,234,234,255435,2,32,23,))