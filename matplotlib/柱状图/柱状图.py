import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] =['SimHei'] # 字体
plt.rcParams['axes.unicode_minus'] =False #处理符号

way = "D:/pandas/01.柱状图.xlsx"
data = pd.read_excel(way)
data.sort_values(by='分数',inplace=True,ascending=False)

plt.bar(data.姓名, data.分数, label='成绩')
plt.xlabel("姓名")
plt.ylabel("分数")
plt.xticks(data.姓名, rotation=45)
plt.ylim([-100, 120])
plt.tight_layout() # 紧凑型布局

plt.legend(loc='lower left') #图标位置
plt.title("Student Grade",fontsize=16, fontweight='bold') # 大标题  大小  粗体
plt.savefig(r'') # 图保存的位置
plt.show()

