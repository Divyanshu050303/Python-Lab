import matplotlib.pyplot as plt
import numpy as np
# first graph
x1=np.array([1, 3, 4, 5])
y1=np.array([3, 5, 1, 6])
plt.subplot(2, 3, 1)
plt.plot(x1, y1)
# second graph
x2=np.array([4, 5, 8, 6])
y2=np.array([3, 6, 1, 7])
plt.subplot(2, 3, 2)
plt.plot(x2, y2)
# third graph
x3=np.array([5, 3, 2, 6])
y3=np.array([1, 6, 3, 2])
plt.subplot(2, 3, 3)
plt.plot(x3, y3)
# fourth graph
x4=np.array([1, 6, 7, 5])
y4=np.array([2, 3, 1, 8])
plt.subplot(2, 3, 4)
plt.plot(x4, y4)
# fifth graph
x5=np.array([2, 7, 4, 3])
y5=np.array([4, 7, 2, 6])
plt.subplot(2, 3, 5)
plt.plot(x5, y5)
# sixth graph
x6=np.array([1, 2, 7, 4])
y6=np.array([9, 7, 2, 8])
plt.subplot(2, 3, 6)
plt.plot(x6, y6)
plt.show()