# syntax
# map(function, iterable(s))


nums = [1, 2, 3, 4, 5]
square = map(lambda x: x *x, nums)  # map(lambda x:
print("The square of list = ", list(square))

# print(type(nums))

# OUTPUT
# he square of list =  [1, 4, 9, 16, 25]
