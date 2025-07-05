import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_excel(r'D:\pandas\17.直方图.xlsx')
cloth, photo = plt.subplots(1, 1)
photo.plot(data.序号, data.身高)
# # 分段
# photo.locator_params('x', nbins=5)
# # 先找轴
# plt.gca().locator_params('x', nbins=5)

# 按照7的倍数
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(7))
# 保留小数
plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
plt.xticks(rotation=45)
plt.show()