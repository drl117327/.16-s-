import matplotlib.pyplot as plt

cloth = plt.figure()
photo = cloth.add_subplot(1,1,1)
# 设置颜色(none：代表消失)
# photo.spines['top'].set_color('none')
photo.spines['right'].set_color('none')
photo.spines['bottom'].set_color('none')
# photo.spines['left'].set_color('none')
# 对y轴进行反转
axis = plt.gca()
axis.invert_yaxis()
# # 取消刻度
# photo.set_xticks([])
# photo.set_yticks([])

# x轴到顶部
photo.xaxis.set_ticks_position('top')
# y轴到右边
photo.yaxis.set_ticks_position('right')
plt.show()