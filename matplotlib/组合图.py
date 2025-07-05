import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.ticker as ticker
plt.rcParams['font.sans-serif'] = ['SimHei']
data = pd.read_excel(r'D:\pandas\09.折线与柱状组合图.xlsx')

cloth = plt.figure()
photo1 = cloth.add_subplot(111)
photo1.bar(data.班级, data.销售量, label='销售量')

photo1.legend(loc='upper left')
# 调整坐标轴刻度
photo1.set_ylim([0, 12500])
# 共享x轴
photo2 = photo1.twinx()

photo2.plot(data.班级, data.毛利率, marker='v', color='r', label='毛利率')
# 百分比标签内
# percentage = mtick.FormatStrFormatter('%.2f%%')
# photo2.yaxis.set_major_formatter(percentage)
# 标签上添加数据
# for x, y in zip(data.班级, data.毛利率2):
#     plt.text(x, y, str(y)+'%', color='b', fontsize=20)

# 需要100%
percentage = ticker.PercentFormatter(1, 2)  # 第一个参数是指定100%，第二个是保留几位小数
photo2.yaxis.set_major_formatter(percentage)
photo2.legend(loc='upper right')
photo2.set_ylim([0, 1])
# 添加标签
for x, y in zip(data.班级, data.毛利率):
    plt.text(x, y, str(round(y*100, 2))+'%', c='b', fontsize=10)
plt.show()
