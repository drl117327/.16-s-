import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
# 画布样式
plt.style.use('ggplot')
x = ['A', 'B', 'C', 'D', 'E', 'F']
y = [1, 10, 7, 5, 11, 6]
# 样式:drawstyle=['steps', 'step-pre', 'steps-mid', 'steps-post']
plt.plot(x, y, drawstyle='steps')
plt.show()