def myfunction(args):
    return lambda a: a * args
mul = myfunction(7)  # mul is now a function that multiplies its argument by 2
print(mul(4))



sum = lambda x, y: (x + y)
print(sum(12,8))
