import matplotlib.pyplot as plt
import numpy as np

y = np.array([45, 70, 80, 92])  # Valores de la variable dependiente (Y)
mylabels = ["C++", "JavaScript", "Java", "Python"]
plt.pie(y, labels=mylabels, startangle=90)
plt.show()