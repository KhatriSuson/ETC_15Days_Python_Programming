import pandas as pd

data = pd.read_excel(
    "E:/BICT/ETC/python_programmin_event/15_Days_Python_Programing/sample_datasets.xlsx"
)

# # Print The excel file data
# print(f"The data of excel file :\n {data}")

# # Printing excel data length
# print(f"The data has {len(data)} rows and {len(data.columns)} columns.\n")

# Print the information of data
# information_of_data = data.info()
# print("Information of Data:\n", information_of_data)


# print(data["cloud"].describe())  # Describing cloud column


# The notna() conditional function returns a True for each row the values are not a Null value.

# It is used to remove or filter out missing (NaN) values in a Pandas dataframe.
# cloud_no_na = data[data["cloud"].notna()]
# print(cloud_no_na)


# Filter the only GitHub cloud

github_cloud = data.loc[data["cloud"] == "GitHub"]
print("\nOnly Github Cloud:\n", github_cloud, "\n")


amazon_cloud = data.loc[data["cloud"] == "Amazon"]
print("\nOnly amazon Cloud:\n", amazon_cloud, "\n")
