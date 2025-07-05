import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
data = pd.read_excel(r'D:\pandas\17.直方图.xlsx')
# bins:组距 facecolor:颜色 edgecolor:边框
plt.hist(data.身高, bins=30, facecolor='r', alpha=0.6, edgecolor='b')

plt.show()