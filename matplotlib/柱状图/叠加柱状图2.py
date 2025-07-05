import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
way = r'D:/pandas/04.堆叠柱状图.xlsx'
data = pd.read_excel(way)
plt.bar(x=0, bottom=data.姓名, height=0.5, width=data.语文, orientation='horizontal', color='red', label='语文')
plt.bar(x=data.语文, bottom=data.姓名, height=0.5, width=data.数学, orientation='horizontal', color='green', label='数学')
plt.bar(x=data.语文+data.数学, bottom=data.姓名, height=0.5, width=data.英语, orientation='horizontal', color='blue', label='英语')

for x1, y1 in enumerate(data.语文):
    plt.text(y1-10, x1, str(y1), color='white', ha='center', va='center', fontsize=20)

for x1, y1 in enumerate(data.语文+data.数学):
    plt.text(y1-10, x1, str(y1), color='white', ha='center', va='center', fontsize=20)

for x1, y1 in enumerate(data.语文+data.数学+data.英语):
    plt.text(y1-10, x1, str(y1), color='white', ha='center', va='center', fontsize=20)

plt.legend()
plt.show()