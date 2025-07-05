import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
way = 'D:/pandas/09.折线与柱状组合图.xlsx'
data = pd.read_excel(way)

bu, photo = plt.subplots(2, 2)  # 几行几列
# 手动调整间距
bu.subplots_adjust(wspace=0.5, hspace=0.3, left=0.125, right=0.9, top=0.9, bottom=0.1)

first = photo[0, 0]
second = photo[0, 1]
third = photo[1, 0]
forth = photo[1, 1]

first.bar(data.班级, data.销售量, color='r', alpha=0.6)
forth.pie(x=data.销售量, labels=tuple(data.班级))

plt.show()