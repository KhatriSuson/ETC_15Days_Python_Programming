# def check_even_number(number):
#     if number % 2 == 0:
#         return number


# numbers = [1, 2, 3, 4, 5, 6, 8]
# new_numbers = []
# for number in numbers:
#     even_num = check_even_number(number)
#     if even_num is not None:
#         new_numbers.append(even_num)
# print(new_numbers)


numbers = [1, 2, 3, 4, 5, 6, 8, 10, 11]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

five_num = filter(lambda x: x < numbers[5], numbers)
print(list(five_num))
