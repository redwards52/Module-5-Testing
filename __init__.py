target = __import__("my_sum.py")
sum = target.sum

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total