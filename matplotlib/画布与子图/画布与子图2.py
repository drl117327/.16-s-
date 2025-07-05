import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
way = 'D:/pandas/09.折线与柱状组合图.xlsx'
data = pd.read_excel(way)
# 画布名字:num 设置大小:figsize 背景颜色：facecolor
bu = plt.figure(num='邓瑞霖', dpi=200)

plt.subplot(2, 2, 1)
plt.bar(data.班级, data.销售量, color='r', alpha=0.6)

plt.subplot(2, 2, 3)
plt.pie(x=data.销售量, labels=tuple(data.班级))

plt.subplot(2, 2, 4)
plt.plot(data.班级, data.毛利率)

# 自动调整布局
plt.tight_layout()
plt.show()