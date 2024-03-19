import matplotlib.pyplot as plt

import numpy as np

x = np.arange(1, 19)
# y = x+np.random.randn()
y = x + 5

plt.plot(x, y, marker="o")
plt.show()
