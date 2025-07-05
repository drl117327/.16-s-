import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
# 样式
plt.style.use('ggplot')

data = pd.read_excel(r'D:\pandas\22.雷达图.xlsx', index_col='姓名')
condition1 = "姓名=='A01'"
condition2 = "姓名=='A02'"
# 加入第一个数据
A01 = data.query(condition1)['分数']
A02 = data.query(condition2)['分数']
subject = data.query(condition1)['科目']

jiaodu = np.linspace(0, 2*np.pi, len(A01), endpoint=False)  # 创建一维数组

# 连接
A01 = np.concatenate((A01, [A01.iloc[0]]))
A02 = np.concatenate((A02, [A02.iloc[0]]))
subject = np.concatenate((subject, [subject.iloc[0]]))
jiaodu = np.concatenate((jiaodu, [jiaodu[0]]))

# 画图
cloth = plt.figure()
# polar制作雷达图
photo = cloth.add_subplot(111, polar=True)
photo.plot(jiaodu, A01, 'ro-', linewidth=2, alpha=0.3, label='A01')
# 填充
photo.fill(jiaodu, A01, 'r-', alpha=0.3)
plt.legend(loc='upper left')
# 标签
photo.set_thetagrids(jiaodu*180/np.pi, subject)
photo.set_ylim([0,100])
plt.show()