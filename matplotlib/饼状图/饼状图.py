import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
way = 'D:/pandas/07.饼图.xlsx'
data = pd.read_excel(way)
# counterclock:顺时针还是逆时针 labeldistance:标签位置 radius:半径
# shadow:显示阴影
plt.pie(x=data.第一次, labels=tuple(data.姓名), labeldistance=0.5, pctdistance=0.3, colors=['r', 'g', 'm'], autopct='%.2f%%', startangle=90, counterclock=False, textprops={'fontsize': 20, 'color': 'w'}, shadow=True)  # explode:分离多少(+)分离 autopct:百分比
plt.pie(x=data.第二次, radius=0.5)
# 将饼图变成正圆
plt.axis('equal')
# 添加图例
# borderaxespad图例内边距 ncol:分裂
plt.legend(loc='upper right', fontsize=10, bbox_to_anchor=(1.1, 1.05), borderaxespad=0.3, ncol=3)

# 保存高清图片 bbox_inches='tight'：忽略不可见的轴
plt.savefig('d:/饼图,jpg', dpi=200, bbox_inches='tight')
plt.show()

