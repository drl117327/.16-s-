import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
way = 'D:/pandas/08.折线图.xlsx'
data = pd.read_excel(way)
# maker:坐标标签
plt.plot(data.时间, data.蔬菜, color='r', marker='*', ms=10)
plt.plot(data.时间, data.水果, color='g', marker='o', ms=10)
plt.plot(data.时间, data.食品, color='b', marker='^', ms=10)
plt.plot(data.时间, data.用品, color='y', marker='v', ms=10)

for z in [data.蔬菜, data.水果, data.食品, data.用品]:
    for x, y in zip(data.时间, z):
        plt.text(x, y+0.3, str(y), ha='center', va='center', fontsize=20, rotation=0)


plt.show()