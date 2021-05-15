import matplotlib.pyplot as plt
import numpy as np
# First graph
x1=np.array([1, 2, 3, 4, 5])
y1=np.array([2, 5, 8, 7, 9])

plt.subplot(1, 2, 1)
plt.plot(x1, y1)
plt.title("SALES")
# Second graph
x2=np.array([1, 2, 3, 4, 5])
y2=np.array([10, 20, 30, 40, 50])
plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.title("INCOME")
plt.suptitle("MY SHOP")
plt.show()