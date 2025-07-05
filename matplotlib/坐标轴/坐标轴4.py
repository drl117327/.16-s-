import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mtl
import datetime as dt
plt.rcParams['font.sans-serif'] = ['SimHei']
data = pd.read_excel(r'D:\pandas\12.日期.xlsx')
plt.plot(data.日期, data.销售)
plt.gca().xaxis.set_major_formatter(mtl.dates.DateFormatter('%Y*%m*%d'))
plt.show()