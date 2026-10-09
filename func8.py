def largest(*args):
    if len(args)==0:
        return None
    else:
        large= args[0]
        for x in args:
            if x>large:
                large = x

    return large

print(largest())