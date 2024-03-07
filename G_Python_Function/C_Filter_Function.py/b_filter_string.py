string_var = "Hello123IamPython0987"

filter_Char = filter(lambda x: not x.isdigit(), string_var)

filter_string = ''.join(filter_Char)
print(filter_string)