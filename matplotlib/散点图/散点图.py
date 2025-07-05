import pandas as pd
import matplotlib.pyplot as plt
# 显示全部的列
# pd.options.display.max_columns=None

plt.rcParams['font.sans-serif'] = ['SimHei']
data = pd.read_excel(r'D:\pandas\16.散点图.xlsx')
# 散点图 s:比重
plt.scatter(data.身高, data.体重, s=data.身高, c=data.身高, marker='o', alpha=0.5)
# 颜色图例
plt.colorbar()
plt.show()