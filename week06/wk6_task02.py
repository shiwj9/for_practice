import numpy as np
import pandas as pd

# numpy操作
print('1.使用Numpy库：')
# 定义数组
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20, 30])

# 利用广播机制将B“广播”到与A相同的形状，并进行对应位置的元素相加?
C = A + B

print("数组C（按行相加的结果）:")
print(C)

# 利用广播机制将B中的第一个元素（10）与A中的每个元素相加
D = A + B[0]

print("数组D（与B中第一个元素相加的结果）:")
print(D)

# pandas操作?
print('2.使用Pandas库：')

# 定义DataFrame
A = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
B = pd.DataFrame({'x': [10], 'z': [20]})

# 利用广播机制（实际上是pandas的对齐机制）进行相加，不同列名保持不变
C = A + B.reindex_like(A).fillna(0)  # 使用reindex_like确保B与A形状相同，并用0填充缺失值

print("DataFrame C（相同列名相加，不同列名保持不变）:")
print(C)
# 计算A中每列的值与B中列'x'的值相加的结果
D = A.copy()
D['x'] = A['x'] + B.reindex_like(A).fillna(0)['x']
D['y'] = A['y'] + B.reindex_like(A).fillna(0)['x']

print("DataFrame D:")
print(D)
