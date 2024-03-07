def square(x):
    return x * x


# Create  a list of numbers to process.

number = [1, 2, 3, 4, 5]

square = map(
    square, number
)  # Apply the 'square' function to each element in the 'number' list.

print("The square of list = ",list(square))  # Convert the result back into a list and print it out.


# OUTPUT
# The square of list =  [1, 4, 9, 16, 25]