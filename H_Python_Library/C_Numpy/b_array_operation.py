import numpy as np

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

# Add two arrays element-wise
result = arr1 + arr2
print(f"Resutl = \n{result}")

# # Matrix multipication
mul = np.dot(arr1, arr2)
print(f"Multiplication: \n{mul}")


# # Array Indexing

index_1 = arr1[0]  # Access first element of array
print(f"\nIndexed value \n {index_1}")

index_2 = arr1[2]
print(f"\n Index value :\n{index_2}")


# # slicing array
sliced_array = np.array(["Hello", "World", "I", "am", "python"])
print("\nSlicing")
print("Full array:\n", sliced_array)
print("From start to third index :\n", sliced_array[0:3])  # From start to third index

first_element = sliced_array[:1]  # Get elements from beginning to the first occurrence of non-True element in
print(first_element)


# # sum of the arraY
array = [1, 2, 3, 4, 5]
sum = np.sum(array)
print(f"The sum of the array \n {sum}")
