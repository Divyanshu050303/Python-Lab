import matplotlib.pyplot as plt
import numpy as np

sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x, y, s=sizes, alpha=0.5)
plt.show()