import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    "E:/BICT/ETC/python_programmin_event/15_Days_Python_Programing/H_Python_Library/D_Pandas/datasets.csv"
)
# print(data)

data.plot()
plt.show()
