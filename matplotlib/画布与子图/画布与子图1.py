import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
way = 'D:/pandas/09.折线与柱状组合图.xlsx'
data = pd.read_excel(way)
# 设置画布:生成一张布
bu = plt.figure()
first = bu.add_subplot(2, 2, 1)  # 两行两列第一个图
second = bu.add_subplot(2, 2, 2)
third = bu.add_subplot(2, 2, 3)
plt.plot(data.班级,data.毛利率, label='毛利率', color='r', marker='*', ms=10)
forth = bu.add_subplot(2, 2, 4)
plt.bar(data.班级, data.销售量,color='r', label='销售量', alpha=0.6)

plt.show()