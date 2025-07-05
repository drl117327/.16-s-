import squarify
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel(r'D:\pandas\29.树状图.xlsx')
color = ['r', 'y', 'b', 'g', 'yellow', 'cyan', 'coral']
photo = squarify.plot(sizes=data.销售数量, label=data.名称, color=color, value=data.销售数量, edgecolor='white',
                      linewidth=3, text_kwargs={'fontsize': 20}) # 字体大小
plt.axis('off')  # 去掉坐标轴
photo.set_title('销售情况', fontdict={'fontsize': 20})
plt.show()