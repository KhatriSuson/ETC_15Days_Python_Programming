import matplotlib

print(matplotlib.__version__)


import matplotlib.pyplot as plt

import numpy as np

x = np.array([2, 4])
y = np.array([10, 10])
plt.plot(x, y, marker="o")
plt.show()

