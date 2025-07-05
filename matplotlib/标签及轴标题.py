import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
cloth = plt.figure()
plt.subplot(221)
plt.plot(['A', 'B', 'C'], [1, 2, 3], 'ro-')
# 添加轴标题 pad:框的大小
dic = dict(facecolor='yellow', pad=5, alpha=0.2)
plt.xlabel('English', bbox=dic)
# 设置标题 fontweight='bold' 加粗
plt.suptitle('photo', fontsize=20, fontweight='bold', color='r')
plt.subplots_adjust(left=0.2, top=0.8, wspace=0.8, hspace=0.8, bottom=0.1)
plt.subplot(222)
plt.subplot(223)
plt.subplot(224)
plt.show()