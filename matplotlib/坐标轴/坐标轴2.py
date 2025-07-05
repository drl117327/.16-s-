import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
way = r'D:\pandas\17.直方图.xlsx'
data = pd.read_excel(way)
cloth, photo = plt.subplots(1,1)
photo.plot(data.序号, data.身高)
plt.gca().get_xticklabels()[2].set(c='r', fontsize=20)

plt.show()
