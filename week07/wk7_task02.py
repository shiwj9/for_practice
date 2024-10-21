import matplotlib.pyplot as plt
import numpy as np
# from mpl_toolkits.mplot3d import Axes3D

# 数据集
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [3, 4, 6, 9, 13]

categories = ['A', 'B', 'C']
values1 = [10, 20, 30]
values2 = [5, 15, 25]

labels = ['A', 'B', 'C', 'D']
sizes = [25, 35, 20, 20]

# 创建一个包含 2 行 2 列的子图
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# （1） 多折线图
axs[0, 0].plot(x1, y1, color='blue', linestyle='-', marker='o', label='Dataset 1')
axs[0, 0].plot(x1, y2, color='green', linestyle='--', marker='s', label='Dataset 2')
axs[0, 0].set_title('Multiple Line Chart')
axs[0, 0].set_xlabel('X-axis')
axs[0, 0].set_ylabel('Y-axis')
axs[0, 0].grid(True)
axs[0, 0].legend()

# （2） 堆叠柱状图
width = 0.35
x = np.arange(len(categories))
axs[0, 1].bar(x, values1, width, label='Values 1', color='blue')
axs[0, 1].bar(x, values2, width, bottom=values1, label='Values 2', color='green')
axs[0, 1].set_title('Stacked Bar Chart')
axs[0, 1].set_xlabel('Categories')
axs[0, 1].set_ylabel('Values')
axs[0, 1].set_xticks(x)
axs[0, 1].set_xticklabels(categories)
axs[0, 1].legend()

# 添加数据标签和百分比显示
for i in range(len(categories)):
    total = values1[i] + values2[i]
    axs[0, 1].text(x[i], total + 1, f'{total}\n({values1[i] / total:.0%}, {values2[i] / total:.0%})', ha='center')


# （3） 环形图
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return f'{pct:.1f}%\n({val})'

    return my_autopct


wedges, texts, autotexts = axs[1, 0].pie(sizes, labels=labels, autopct=make_autopct(sizes), startangle=140,
                                         wedgeprops=dict(width=0.3, edgecolor='w'))
plt.setp(autotexts, size=10, weight="bold")
axs[1, 0].set_title('Donut Chart')

# 设置环形图中心留空
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# （4） 3D 曲面图
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))

ax = axs[1, 1].projection_3d = fig.add_subplot(224, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('3D Surface Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# 调整布局
plt.tight_layout()

# 保存图表
plt.savefig('charts.png')

# 显示图表（可选，用于调试）
plt.show()