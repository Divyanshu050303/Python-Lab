import matplotlib.pyplot as plt
import numpy as np
# first graph
x1=np.array([1, 4, 6, 3])
y1=np.array([3, 8, 1, 10])
plt.subplot(2, 1, 1)
plt.plot(x1, y1)
# second graph
x2=np.array([4, 2, 6, 1])
y2=np.array([10, 20, 30, 40])
plt.subplot(2, 1, 2)
plt.plot(x2, y2)

plt.show()