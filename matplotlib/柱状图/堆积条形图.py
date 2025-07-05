import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

way = r'D:\pandas\04.堆叠柱状图.xlsx'
data = pd.read_excel(way)

plt.bar(np.arange(9), data.语文, color='red', label='语文')
plt.bar(np.arange(9), data.数学, bottom=data.语文, color='blue', label='数学')
plt.bar(np.arange(9), data.数学, bottom=data.语文+data.数学, color='green', label='英语')
# x轴标签
plt.xticks(np.arange(9), data.姓名, rotation=45)
# 图例 位置居中，列改为3列
plt.legend(loc='upper center', ncol=3)
# y轴刻度
plt.ylim([10,350])
# 加网格线
# plt.grid()
# 数据标签
for x1, y1 in enumerate(data.语文):
    plt.text(x1, y1-10, str(y1), color='white', fontsize=20, ha='center')
for x1, y1 in enumerate(data.语文+data.数学):
    plt.text(x1, y1-10, str(y1), color='white', fontsize=20, ha='center')
for x1,y1 in enumerate(data.语文+data.数学+data.英语):
    plt.text(x1, y1-10, str(y1), color='white', fontsize=20, ha='center')

plt.show()
