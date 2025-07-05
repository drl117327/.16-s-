import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

way = 'D:/pandas/03.分组柱状图.xlsx'
data = pd.read_excel(way)
data.sort_values(by="第二年",inplace=True, ascending=False)
width = 0.3
data['第一年'].values.tolist() # 转换成列表
plt.bar(x=data.姓名, height=data.第一年, color='red', width=width, label="第一年")
plt.bar(x=np.arange(len(data.姓名))+width, height=data.第二年, color='blue', width= width, label="第二年")

plt.xticks(data.姓名)
# 对轴进行操作
axis = plt.gca()
# 对x轴数据进行旋转45度，且以中心为旋转点【同样可以用left或right】
axis.set_xticklabels(data.姓名, rotation=45, ha='center')
plt.legend()
# 解决图四周的空白，是对图形操作，需要先拿到图形[也可以用紧凑型布局方案]
photo = plt.gcf()  #拿到图形
photo.subplots_adjust(left=0.1, bottom=0.3)

# 第一个下标是索引， 第二个下标是列表的内容
for x, y1 in enumerate(data.第一年):
    plt.text(x,y1,str(y1), fontsize=10, rotation=0, ha='center', va='bottom')

for x, y1 in enumerate(data.第二年):
    plt.text(x+width, y1, str(y1), fontsize=10, rotation=0, ha='center', va='bottom')

# 紧凑型的布局
#plt.tight_layout()

plt.show()
