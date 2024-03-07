def start_with_A(s):
    return s[0] == "A"


fruit = ["Apple", "Banana", "Apricot", "Chery", "A_mango"]

map_obj = map(start_with_A, fruit)
print("Using 'start_with_A' funciton = ", list(map_obj))

# output
# Using 'start_with_A' funciton =  [True, False, True, False, True]


map_obj1 = map(lambda s: s[0] == "A", fruit)
print("Using lambda function =", list(map_obj1))

# # using for loop