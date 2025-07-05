import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

way = 'D:/pandas/09.折线与柱状组合图.xlsx'
data = pd.read_excel(way)
plt.bar(data.班级, data.销售量, color='r', label='销售量', alpha=0.6)
# 显示图例
plt.legend()
# 平均线
average = np.mean(data.销售量)
plt.axhline(average, color='b', linestyle=':')

plt.show()
