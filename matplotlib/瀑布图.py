import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel(r'D:\pandas\28.瀑布图.xlsx')
lis = np.arange(len(data.金额), dtype=np.float64)
bottom = 0

for i in data.金额.index:
    x = lis[i]
    y = data.金额[i]
    if data.金额[i]>= 0:
        win = plt.bar(x, y, 0.8, align='center', bottom=bottom, label='win', color='r')
    else:
        lose = plt.bar(x, y, 0.8, align='center', bottom=bottom, label='lose', color='g')

    bottom += y
    x += 0.8

plt.gca().yaxis.grid(True, linestyle='--', color='grey', alpha=0.25)
# 修改日期格式
date = [d.strftime('%Y-%m-%d') for d in data.日期]
plt.xticks(np.arange(len(data.金额)), date, rotation=45)
plt.show()
