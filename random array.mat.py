import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=100)
y = np.random.randint(100, size=100)
colors = np.random.randint(100, size=100)
sizes = 10 * np.random.randint(100, size=100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()