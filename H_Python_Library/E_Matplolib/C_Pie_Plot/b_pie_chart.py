import matplotlib.pyplot as plt

y = ["A", "B", "C", "D", "E"]
x = [10, 24, 35, 89, 76]

plt.pie(x, labels=y, autopct="%1.1f%%", startangle=45)

plt.title("Pie Chart")

plt.show()



