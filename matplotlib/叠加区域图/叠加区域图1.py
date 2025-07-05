import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_excel(r'D:\pandas\08.折线图.xlsx')
plt.plot(data.时间, data.蔬菜)
plt.plot(data.时间, data.水果)

# 覆盖区域 覆盖下限 覆盖上限 facecolor:颜色
plt.fill_between(data.时间, 0, data.蔬菜, facecolor='r', alpha=0.3)
plt.fill_between(data.时间, data.蔬菜, data.水果,facecolor='g', alpha=0.3)

plt.show()