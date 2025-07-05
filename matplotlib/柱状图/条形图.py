import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']

way = "D:/pandas/01.柱状图.xlsx"
data = pd.read_excel(way)
data.sort_values(by='分数', inplace=True, ascending=False)

plt.bar(x=0,bottom=data.姓名, height=0.5, width=data.分数, color='red',orientation='horizontal', alpha=0.5)
plt.yticks(data.姓名,rotation=45)
plt.xlabel("分数",fontsize=20)
plt.ylabel("姓名",fontsize=20)

plt.title("Student Grade", fontsize=16, fontweight='bold')
plt.show()