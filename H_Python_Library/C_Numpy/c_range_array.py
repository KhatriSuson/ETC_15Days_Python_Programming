import numpy as np
a = np.arange(10)  # range()
print(a)

# 2D array in range
b = np.arange(15).reshape(3, 5)
print(b)

# 3D array in range
c = np.arange(30).reshape(2, 3, 5)
print("3D array\n", c)
# Sort array
array = np.array([1, 4, 2, 6, 3, 5])
sort_array = np.sort(array)
print("The sort array  is \n ", sort_array)

# slicing
slice_array = np.arange(10) ** 2
print("The array is\n", slice_array)
print(" every second element from the beginning of the list\n", slice_array[::2], "\n")  # get every second element from the beginning of the list
print("Sliceing array is\n", slice_array[2:7])

for i in slice_array:
    print(i, "\t", i * 2)
