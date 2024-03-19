import matplotlib.pyplot as plt

import numpy as np

# Data

np.random.seed(0)
data = np.random.randn(1000)

# Plot the histrogram

plt.hist(data, bins=30, color="black", edgecolor="green")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram Demonstrates ")
plt.show()
