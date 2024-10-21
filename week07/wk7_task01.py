import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 设置字体为 SimHei 显示中文标签，(Windows 系统)
rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# (1)
# 数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 绘制折线图
plt.plot(x, y, label='数据序列')

# 设置标题和轴标签
plt.title('折线图示例')
plt.xlabel('时间')
plt.ylabel('值')

# 添加图例
plt.legend()

# 开启网格
plt.grid(True)

# 保存图表
plt.savefig('line_chart.png')

# 显示图表
plt.show()

# (2)
# 数据
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
colors = ['red', 'blue', 'green', 'purple']

# 绘制柱状图
plt.bar(categories, values, color=colors)

# 添加数据标签
for i, v in enumerate(values):  # i,v分别是索引和值
    # (数据标签的x坐标位置、数据标签的y坐标位置、要显示的文本内容、水平对齐、和垂直对齐方式)
    plt.text(i, v + 1, str(v), ha='center', va='bottom')

# 设置标题和轴标签（对于柱状图，x轴通常是类别标签，所以不需要设置x轴刻度）
plt.title('柱状图示例')
plt.ylabel('值')

# 保存图表
plt.savefig('bar_chart.png')

# 显示图表
plt.show()

# (3)
# 随机生成数据
np.random.seed(0)  # 设置随机种子以便结果可重复
x_random = np.arange(1, 101)
y_random = np.random.rand(100) * x_random  # 假设有一定的线性关系

# 绘制散点图
plt.scatter(x_random, y_random, color='blue', s=10, alpha=0.5, label='数据点')

# 计算趋势线（线性回归）
coefficients = np.polyfit(x_random, y_random, 1)
polynomial = np.poly1d(coefficients)
trendline_x = np.linspace(1, 100, 100)
trendline_y = polynomial(trendline_x)

# 绘制趋势线
plt.plot(trendline_x, trendline_y, color='red', label='趋势线')

# 设置标题和轴标签
plt.title('散点图及趋势线示例')
plt.xlabel('x 值')
plt.ylabel('y 值')

# 添加图例
plt.legend()

# 保存图表
plt.savefig('scatter_chart.png')

# 显示图表
plt.show()

# (4)
# 数据
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # 突出显示第一个扇区

# 绘制饼图
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        startangle=140)  # autopct 用于显示百分比，startangle 设置起始角度

# 设置标题（对于饼图，通常不需要x轴和y轴标签）
plt.title('饼图示例')

# 确保饼图是圆形的（等比例）
plt.axis('equal')

# 保存图表
plt.savefig('pie_chart.png')

# 显示图表
plt.show()
