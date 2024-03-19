import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D", "E"]
values = [10, 24, 35, 89, 76]

plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=45)

plt.title("Pie Chart")

plt.show()


import qrcode
