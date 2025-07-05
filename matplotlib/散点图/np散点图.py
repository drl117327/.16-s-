import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
k = 500
x = np.random.rand(k)
y = np.random.rand(k)
size = np.random.rand(k)*50
color = np.arctan2(x, y)
plt.scatter(x, y, s=size, c=color)

plt.colorbar()
plt.show()