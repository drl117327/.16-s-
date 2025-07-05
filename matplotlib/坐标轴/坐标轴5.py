import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_excel(r'D:\pandas\08.折线图.xlsx')
plt.plot(data.时间, data.蔬菜)
# plt.gca().set_xlim([0,10])
# plt.gca().set_ylim([0,10])
# plt.gca().axis([0, 10, 0, 30])
plt.gca().set_ylim(bottom=-10)  # 下限
plt.gca().set_xlim(left=-10)  # 左边界
plt.show()