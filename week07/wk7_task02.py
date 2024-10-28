import matplotlib.pyplot as plt  # 导入 matplotlib 库，用于绘制图表
import numpy as np  # 导入 numpy 库，用于生成数据和处理数组
from matplotlib import rcParams  # 导入 rcParams 用于配置图表字体等属性

# from mpl_toolkits.mplot3d import Axes3D  # 这是一个可选的 3D 库的导入，3D 图形需要用到

# 设置字体为 SimHei 以支持中文显示，特别是对于 Windows 系统
# 'font.sans-serif' 用于设置默认字体为 SimHei（黑体），以显示中文
rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# 'axes.unicode_minus' 设置为 False，确保负号能够正确显示
rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 数据集
# 创建用于多折线图的 x 和 y 数据
x1 = [1, 2, 3, 4, 5]  # x 轴数据，代表不同的点
y1 = [2, 3, 5, 7, 11]  # y 轴数据，代表第一个数据集的值
y2 = [3, 4, 6, 9, 13]  # y 轴数据，代表第二个数据集的值

# 堆叠柱状图的数据
categories = ['A', 'B', 'C']  # 柱状图的类别标签
values1 = [10, 20, 30]  # 第一个类别的值
values2 = [5, 15, 25]  # 第二个类别的值

# 环形图的数据
labels = ['A', 'B', 'C', 'D']  # 环形图的标签
sizes = [25, 35, 20, 20]  # 每个部分的大小（比例）

# 创建一个包含 2 行 2 列的子图布局，每个子图会放置不同的图表
fig, axs = plt.subplots(2, 2, figsize=(14, 10))  # 设置子图的总大小为 14x10 英寸

# （1） 多折线图
# 在第一个子图（第 0 行，第 0 列）中绘制多折线图
axs[0, 0].plot(x1, y1, color='blue', linestyle='-', marker='o', label='Dataset 1')  # 绘制第一个数据集的折线图，蓝色实线和圆形标记
axs[0, 0].plot(x1, y2, color='green', linestyle='--', marker='s', label='Dataset 2')  # 绘制第二个数据集的折线图，绿色虚线和方形标记
axs[0, 0].set_title('Multiple Line Chart')  # 设置子图的标题
axs[0, 0].set_xlabel('X-axis')  # 设置 x 轴标签
axs[0, 0].set_ylabel('Y-axis')  # 设置 y 轴标签
axs[0, 0].grid(True)  # 设置网格线
axs[0, 0].legend()  # 显示图例

# （2） 堆叠柱状图
bar_width = 0.5  # 设置柱子的宽度
index = np.arange(len(categories))  # 生成柱状图的 x 轴位置（每个类别的位置）
# 使用 bar() 函数绘制堆叠柱状图，第一个数据集绘制在底部
axs[0, 1].bar(index, values1, bar_width, color='blue', label='类别 1')  # 绘制第一个类别的柱子，蓝色
# 第二个数据集绘制在第一个数据集之上（通过 bottom 参数实现堆叠）
axs[0, 1].bar(index, values2, bar_width, bottom=values1, color='green', label='类别 2')  # 绘制第二个类别的柱子，绿色

# 在每个堆叠柱子的正中间显示总值和百分比
for i in range(len(categories)):
    total = values1[i] + values2[i]  # 计算总值
    # 在柱子上方显示总值和每个类别的百分比
    axs[0, 1].text(i, values1[i] + values2[i] / 2,  # 在柱子中间位置显示文本
                   f'{total}\n({values1[i] / total * 100:.2f}%, {values2[i] / total * 100:.2f}%)',  # 显示总值和百分比
                   ha='center',  # 水平居中
                   va='center')  # 垂直居中

# 设置堆叠柱状图的标题、x 轴和 y 轴标签
axs[0, 1].set_title('堆叠柱状图')  # 设置子图的标题
axs[0, 1].set_xlabel('类别')  # 设置 x 轴标签
axs[0, 1].set_ylabel('值')  # 设置 y 轴标签
axs[0, 1].legend()  # 显示图例
axs[0, 1].set_xticks(index, categories)  # 设置 x 轴刻度，并将类别标签显示在相应位置

# （3） 环形图
# 绘制一个环形图，类似于饼图，但是通过 wedgeprops 参数设置宽度来实现环形效果
wedges, texts, autotexts = axs[1, 0].pie(sizes,  # 环形图每部分的大小
                                         labels=labels,  # 设置每个部分的标签
                                         wedgeprops=dict(width=0.3, edgecolor='w'),  # 设置环形宽度和边缘颜色
                                         startangle=90,  # 从 90 度开始绘制
                                         autopct='%1.1f%%',  # 自动显示百分比，保留一位小数
                                         colors=['blue', 'green', 'red', 'orange'])  # 每个部分的颜色
axs[1, 0].set(aspect="equal")  # 设置为等宽高比例以确保圆形外观
axs[1, 0].set_title('环形图')  # 设置子图标题

# 给每个 wedge（环形部分）设置边框颜色和宽度
for wedge in wedges:
    wedge.set_edgecolor('black')  # 设置边缘颜色为黑色
    wedge.set_linewidth(1)  # 设置边缘线条宽度为 1

# （4） 3D 曲面图
# 创建用于 3D 曲面图的 x, y 坐标网格
X = np.linspace(-5, 5, 100)  # 在 -5 到 5 之间生成 100 个均匀分布的点，作为 X 轴的值
Y = np.linspace(-5, 5, 100)  # 在 -5 到 5 之间生成 100 个均匀分布的点，作为 Y 轴的值
X, Y = np.meshgrid(X, Y)  # 生成一个二维网格坐标，X 和 Y 坐标的组合
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))  # 计算 Z 值，Z 是 X 和 Y 的函数，用于生成曲面

# 在第四个子图（第 1 行，第 1 列）中绘制 3D 曲面图
axs[1, 1] = plt.subplot(2, 2, 4, projection='3d')  # 为第四个子图设置 3D 投影
axs[1, 1].plot_surface(X, Y, Z, cmap='viridis')  # 使用 viridis 颜色映射绘制 3D 曲面
axs[1, 1].set_title('3D 曲面图')  # 设置子图的标题
axs[1, 1].set_xlabel('X 轴')  # 设置 X 轴标签
axs[1, 1].set_ylabel('Y 轴')  # 设置 Y 轴标签
axs[1, 1].set_zlabel('Z 轴')  # 设置 Z 轴标签

# 调整子图布局以防止重叠
plt.tight_layout()  # 自动调整子图之间的间距，确保布局不会重叠

# 保存图表到文件
plt.savefig('charts.png')  # 将生成的图表保存为 PNG 格式文件

# 显示图表（可选，用于调试）
plt.show()  # 显示生成的图表