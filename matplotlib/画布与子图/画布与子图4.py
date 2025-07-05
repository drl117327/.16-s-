import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
way = 'D:/pandas/09.折线与柱状组合图.xlsx'
data = pd.read_excel(way)

cloth = plt.figure()
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
# 参数是一个列表，距左和下的距离，以及自身的宽和高度
photo1 = cloth.add_axes([left, bottom, width, height])
photo1.bar(data.班级, data.销售量)
photo1.set_title('销售量')
left, bottom, width, height = 0.65, 0.6, 0.25, 0.25
photo2 = cloth.add_axes([left, bottom, width, height])

photo2.plot(data.班级, data.毛利率 )
photo2.set_title('毛利率')
plt.show()
