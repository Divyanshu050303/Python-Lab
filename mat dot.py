import matplotlib.pyplot as plt
import numpy as np
import random
x1=random.randint(1, 4)
y1=random.randint(3, 8)
x=np.array(x1)
y=np.array(y1)
plt.plot(x, y, "o")
plt.show()