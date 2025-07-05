import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.array([i for i in range(30)])
y = np.random.rand(30)

lis = [[1, 6], [10, 12], [20, 23], [26, 28]]
plt.plot(x, y, 'r')

# 高量显示
for i in lis:
    plt.fill_between(x[i[0]:x[i[1]]], 0, 1, facecolor='r', alpha=0.3)

plt.show()
