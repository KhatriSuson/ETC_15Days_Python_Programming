import numpy as np

array = np.arange(1, 20)
print(f"Original array: {array}")


# Filtering elements

filter = array[array % 2 == 0]
print(f"Fitlert element:\n", filter)


print("Filter elements greater than 10\n", array[array > 10])
