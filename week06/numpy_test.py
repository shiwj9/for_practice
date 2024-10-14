import numpy as np

# 张量生成
# arr = np.zeros((3, 4))
# print(arr)
#
# arr1 = np.array([1, 2, 3, 4], dtype=np.float32)
# print(arr1)

# 属性操作
# arr2 = np.array([[1, 2], [3, 4]])
#
# print(arr2.ndim)
# print(arr2.shape)
# print(arr2.size)
# print(arr2.dtype)#元素数据类型
# print(arr2.itemsize)# 每个元素字节大小
# print(arr2.nbytes)
# print(arr2.T)  # 转置
# print(arr2.data)

# 索引
arr_2d = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(arr_2d[[0, 1, 2], [0, 1, 0]])

