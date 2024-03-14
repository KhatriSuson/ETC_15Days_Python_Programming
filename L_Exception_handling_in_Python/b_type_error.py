try:

    var = "hello" + 32

except TypeError as e:
    print(f"Caught an error: {str(e)}")


try:


    var = len(23)

except TypeError as e:
    print(f"Catch an error : {str(e)}")


# var = "hello" + 32

# print(var)