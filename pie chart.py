import matplotlib.pyplot as plt
import numpy as np
x=np.array([25, 30, 35, 10])
title=["cherry", "banana", 'grapes', 'data']
mycolors = ["r", "y", "g", "k"]
myexplode=[0.2, 0, 0, 0]
plt.pie(x, labels=title, explode=myexplode, shadow=True, colors=mycolors)
plt.legend(title="Four fruit")
plt.show()