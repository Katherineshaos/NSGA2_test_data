import matplotlib.pyplot as plt
import numpy as np
'''
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
'''
'''
plt.plot([1,2,3,4,5],[1,4,9,10,16],'ro')
plt.axis([0,8,0,22])#[xmin,xmax,ymin,ymax]设置x，y轴长度
plt.show()
'''
'''
fig = plt.figure()                      # 创建一个没有 axes 的 figure
fig.suptitle('No axes on this figure')  # 添加标题以便我们辨别

fig, ax_lst = plt.subplots(2, 2)        # 创建一个以 axes 为单位的 2x2 网格的 figure
plt.show()
'''
'''
x = np.linspace(-2, 6, 10)
y1 = x + 3      # 曲线 y1
y2 = 3 - x      # 曲线 y2
plt.figure()    # 定义一个图像窗口
plt.plot(x, y1) # 绘制曲线 y1
plt.plot(x, y2) # 绘制曲线 y2
plt.show()
'''

# 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
plt.figure(figsize=(8, 6), dpi=80)

# 再创建一个规格为 1 x 1 的子图
plt.subplot(111)

x = np.linspace(-2, 6, 50)
y1 = x + 3        # 曲线 y1
y2 = 3 - x        # 曲线 y2

# 绘制颜色为蓝色、宽度为 1 像素的连续曲线 y1
#plt.plot(x, y1, color="blue", linewidth=1.0, linestyle="-")
# 绘制颜色为紫色、宽度为 2 像素的不连续曲线 y2
#plt.plot(x, y2, color="#800080", linewidth=2.0, linestyle="--")

# 绘制颜色为蓝色、宽度为 1 像素的连续曲线 y1
plt.plot(x, y1, color="blue", linewidth=1.0, linestyle="-", label="y1")
# 绘制散点(3, 6)
plt.scatter([3], [6], s=30, color="blue")      # s 为点的 size
# 对(3, 6)做标注
plt.annotate("(3, 6)",
             xy=(3.3, 5.5),       # 在(3.3, 5.5)上做标注
             fontsize=16,         # 设置字体大小为 16
             xycoords='data')  # xycoords='data' 是说基于数据的值来选位置
#scatter() 是用于绘制散图，这里我们只是用其来绘制单个点。
#scatter() 函数必须传入两个参数 x 和 y。
# 值得注意得是，它们的数据类型是列表。
# x 代表要标注点的横轴位置，y 代表要标注点的横轴位置。
# x 和 y 列表中下标相同的数据是对应的。
# 例如 x 为 [3, 4]，y 为 [6, 8]，这表示会绘制点（3，6），（4， 8）。
# 因此，x 和 y 长度要一样。

#annotate函数同样也有两个必传参数，一个是标注内容，另一个是 xy。
# 标注内容是一个字符串。xy 表示要在哪个位置（点）显示标注内容。
# xy 位置地选定。一般是在scatter() 绘制点附近，但不建议重合，这样会影响美观。



# 绘制颜色为紫色、宽度为 2 像素的不连续曲线 y2
plt.plot(x, y2, color="#800080", linewidth=2.0, linestyle="--", label="y2")
# 绘制散点(3, 0)
plt.scatter([3], [0], s=50, color="#800080")
# 对(3, 0)做标注
plt.annotate("(3, 0)", xy=(3.3, 0))
plt.text(4, -0.5, "this point very important",
         fontdict={'size': 12, 'color': 'green'})  # fontdict设置文本字体
#如果你还想给点添加注释。这需要使用text()函数。
# text(x，y，s) 作用是在点(x，y) 上添加文本 s。
# matplotlib 目前好像对中午支持不是很友好， 中文均显示为乱码。


plt.legend(loc="upper left")
#如果需要在图的左上角添加一个图例。我们只需要在 plot() 函数里以「键 - 值」的形式增加一个参数。
# 首先我们需要在绘制曲线的时候，增加一个 label 参数，然后再调用 plt.legend() 绘制出一个图例。
# plt.legend() 需要传入一个位置值



# 设置横轴的上下限
plt.xlim(-1, 6)
# 设置纵轴的上下限
plt.ylim(-2, 10)

# 设置横轴精准刻度
#plt.xticks([-1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5])
# 设置纵轴精准刻度
#plt.yticks([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

plt.xticks([-1, 0, 1, 2, 3, 4, 5, 6],
           ["-1m", "0m", "1m", "2m", "3m", "4m", "5m", "6m"])
# 设置纵轴精准刻度
plt.yticks([-2, 0, 2, 4, 6, 8, 10],
           ["-2m", "0m", "2m", "4m", "6m", "8m", "10m"])

# 设置横轴标签
plt.xlabel("X")
# 设置纵轴标签
plt.ylabel("Y")

plt.show()