import matplotlib.pyplot as plt

import numpy as np

data = {"a": np.arange(50), "b": np.random.randint(0, 50, 50), "c": np.random.randn(50)}

data["d"] = data["a"] + 10 * np.random.randn(50)
data["c"] = np.abs(data["d"]) * 100

# Scatter  plot of 'a' vs 'b', color
# plt.scatter("a", "b", c="c", s="d", data=data)

# Plot
plt.plot("a", "b", c="c", data=data)
plt.xlabel("entry a")
plt.ylabel("entry b")
plt.show()
