import matplotlib.pyplot as plt
import numpy as np

x = np.array([3, 4, 5, 6, 7, 2, 12])
y = np.array([34, 45, 65, 23, 76, 24, 98])

plt.title("Scater Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.scatter(
    x,
    y,
    c=[
        "#00ff01",
        "#ab0101",
        "#abef01",
        "#ab5601",
        "#ab8901",
        "#a21f01",
        "#a23f01",
    ],
)
plt.show()
