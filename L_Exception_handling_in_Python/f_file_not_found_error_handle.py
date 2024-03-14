import os

try:

    os.remove("aaaappple.txt")

except FileNotFoundError as e:
    print(f"Error occure : {str(e)}")


try:
    files = os.listdir("mmmmppp_dir")

except FileNotFoundError as e:
    print(f"Second error occure: {str(e)}")
