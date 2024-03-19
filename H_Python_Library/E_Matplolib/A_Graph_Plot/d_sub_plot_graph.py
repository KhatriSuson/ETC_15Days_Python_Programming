import matplotlib.pyplot as plt

import numpy as np

# First plot
x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])

plt.subplot(1, 2, 1)  # ( row, col, index)
plt.plot(x, y)


# Second Plot

x = np.array([0, 1, 2, 3, 4, 5, 6])
y = x + 3

plt.subplot(1, 2, 2)
plt.plot(x, y, marker="o")
# Adding labels and title to the plots    # |   |
plt.title("Adding Labels & Title")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
print("Done")
# Showing the plot
plt.show()
