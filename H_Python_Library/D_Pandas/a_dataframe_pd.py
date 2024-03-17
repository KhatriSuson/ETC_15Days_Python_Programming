import pandas

print(pandas.__version__)



import pandas as pd

data = pd.DataFrame(
    {
        "Name": ["Ram Rai", "Sita Thapa", "Hari Shah", "Gita Bhujel"],
        "Age": [23, 32, 45, 19],
        "Gender": ["Male", "Female", "Male", "Female"],
    }
)

print("The DataFrame is :\n", data)

print(" Age\n", data["Age"])


gender = pd.Series(["Male", "Female", "Male", "Female"], name="Gender")
print(f"The series of Age \n {gender}")


age = pd.Series(data["Age"])
print(f"The series of age \n {age}")

max_age = data["Age"].max()
print(f"The maximum age is :\n {max_age}")
# print(age.max())


# # discribe()

describe = data.describe()
print(f" Descrice the details of data : \n {describe}")
