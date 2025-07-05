import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
way = r'D:\pandas\12.日期.xlsx'
data = pd.read_excel(way)
# 日期格式化
date = [d.strftime('%m-%d') for d in data.日期]
plt.plot(date, data.销售)
plt.xticks(date, rotation=45)
# 网格线 linestyle:形状  linewidth：宽度
plt.grid(axis='x', color='r', linestyle=':', linewidth=1)

plt.show()