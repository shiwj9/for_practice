import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], color=(0.2, 0.1, 0.7), linestyle='--', linewidth=2, marker='v', markersize=6)

# plt.rcParams['font.family']='SimHei'
plt.title("for test()")

plt.xlabel("x")
plt.ylabel("y")

# 图例
plt.legend("num")

# 任意位置添加文本
plt.text(1, 2, 'key point')

# 轴、刻度等
plt.xlim(1, 4)
plt.grid(True)

plt.show()
