import numpy as np

print('1.创建操作:')
# (1) 产生一个随机整数数组a,大小为 3x2，取值范围为1到10。
a = np.random.randint(1, 11, size=(3, 2))
print("数组a:")
print(a)

# (2) 产生一个2行3列均匀分布随机数组b，取值范围为[0-100]?
b = np.random.uniform(0, 100, size=(2, 3))
print("数组b:")
print(b)

# (3) 产生一个3行3列标准正态分布随机数组c。
c = np.random.randn(3, 3)
print("数组c:")
print(c)

# (4) 产生一个5行3列的均值为10，标准差为10的正态分布数组d; 并输入实际均值和标准差。
d = np.random.normal(10, 10, size=(5, 3))
print("数组d:")
print(d)
mean_d = np.mean(d)
std_d = np.std(d)
print(f"数组d的实际均值: {mean_d}")
print(f"数组d的实际标准差: {std_d}")

# (5) 建立一个数组e，值为（[[1,2,3,4],[5,6,7,8],[9,10,11,12]]）,输出下标为（2，3），（0，0）这两个数组元素的值。
e = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("数组e:")
print(e)
element_2_3 = e[2, 3]
element_0_0 = e[0, 0]
print(f"下标为（2，3）的元素值: {element_2_3}")
print(f"下标为（0，0）的元素值: {element_0_0}")

# 一维数组索引与修改操作
print('\n2.一维数组索引与修改操作：')
arr = np.arange(1, 20, 1)
print(f"一维数组：{arr}")
print(f"索引号为9的元素{arr[9]}")
print(f"索引号从4开始，到9结束的元素:{arr[4:10:1]}")
arr[0:19:2] = 50  # 设置该数组中索引号从1开始，到18结束，间隔为2的一系列元素为50
print(f"修改后:{arr}")

# 二维数组索引与修改操作
print('\n3.二维数组索引与修改操作：')
# (1) 生成1到24之间的6行4列的二维数组，并输出显示
# 使用np.arange(1, 25)生成1到24的数组，然后使用reshape将其转换为6行4列的二维数组
array_2d = np.arange(1, 25).reshape(6, 4)
print("二维数组:")
print(array_2d)

# (2) 访问数组中的元素
# 第0行的数据元素
print("第0行的数据元素:")
print(array_2d[0, :])

# 前三行数据元素
print("前三行数据元素:")
print(array_2d[:3, :])

# 第1行第2列中的元素
print("第1行第2列中的元素:")
print(array_2d[0, 1])

# (3) 对该数组进行转置
transposed_array = array_2d.T
print("转置后的数组:")
print(transposed_array)

# 创建数组并计算
print('\n4.创建数组并计算:')
# 定义数组
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# （1）求数组按行累加和  (axis=1是行方向，0是列方向)
row_sums = np.sum(array, axis=1)
print("按行累加和的结果:")
print(row_sums)  # 输出: [ 6 15 24]

# （2）求数组按列累加和
col_sums = np.sum(array, axis=0)
print("按列累加和的结果:")
print(col_sums)  # 输出: [12 15 18]

# （3）求数组按行累积
row_cumsums = np.cumsum(array, axis=1)
print("按行累积的结果:")
print(row_cumsums)
# 输出:
# [[ 1  3  6]
#  [ 4  9 15]
#  [ 7 15 24]]

# （4）求数组按列累积
col_cumsums = np.cumsum(array, axis=0)
print("按列累积的结果:")
print(col_cumsums)
# 输出:
# [[ 1  2  3]
#  [ 5  7  9]
#  [12 15 18]]

# （5）进行每行排序，每行从左到右依次增大
sorted_rows = np.sort(array, axis=1)
print("每行排序后的结果:")
print(sorted_rows)
# 输出:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]]
