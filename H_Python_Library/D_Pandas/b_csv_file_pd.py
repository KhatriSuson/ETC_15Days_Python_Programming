import pandas as pd

data = pd.read_csv(
    "E:/BICT/ETC/python_programmin_event/15_Days_Python_Programing/H_Python_Library/D_Pandas/datasets.csv"
)
print(f"The data  of CSV :\n {data}")

head = data.head(10)
# print(f"The head to elements of CSV file :\n {head}")

tail = data.tail(5)
print(f"The tail elements of CSV file :\n{tail}\n")

# Print the data types of the DataFrame
print(data.dtypes)


# Writing DataFrame to a CSV file

data.to_csv('sample_datasets.csv', index= False)


# Writring DataFrame to a Excel File

data.to_excel("try_to_convert_excel.xlsx", sheet_name="Sheet1")
