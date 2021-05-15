import matplotlib.pyplot as plt
import numpy as np
# first graph
x1=np.array([1, 4, 6, 3])
y1=np.array([4, 2, 7, 1])
plt.subplot(1, 2, 1)
plt.plot(x1, y1)
# second graph
x2=np.array([4, 2, 6, 1])
y2=np.array([4, 3, 7, 2])
plt.subplot(1, 2, 2)
plt.plot(x2, y2)

plt.show()