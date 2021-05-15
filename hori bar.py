import matplotlib.pyplot as plt
import numpy as np
x=np.array(["A", "B", "C", "D"])
y=np.array([8, 10, 2, 6])
plt.barh(x, y, color='r', height=0.1)
plt.show()