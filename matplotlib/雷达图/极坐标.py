import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 风格
jiao = np.array([0.25, 0.75, 1, 1.5, 0.25])
rou = [20, 60, 40, 80, 20]
# 第一个参数是极角，第二个参数是极轴
# np.pi是Π
plt.polar(jiao*np.pi, rou, 'ro-')  # 圆盘
# 填充
plt.fill(jiao*np.pi, rou, 'r', alpha=0.3)
plt.ylim(0, 100)
plt.show()

