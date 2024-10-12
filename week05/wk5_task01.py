# 通过逐项取消注释，编译运行可以显示出错误类型
# SyntaxError
# print("Hello, World!"  # 缺少右括号

# IndentationError
# def say_hello():
# print("Hello, World!")  # 缩进错误

# TypeError
# print(1 + "2")  # 试图将整数和字符串相加

# ValueError
# int("abc")  # 试图将非数字字符串转换为整数

# IndexError
my_list = [1, 2, 3]
# print(my_list[3])  # 索引3超出范围

# KeyError
my_dict = {"a": 1, "b": 2}


# print(my_dict["c"])  # 键"c"不存在

# AttributeError
class MyClass:
    pass


obj = MyClass()
# print(obj.my_attribute)  # 属性"my_attribute"不存在

# ZeroDivisionError
# result = 1 / 0  # 除以零

# FileNotFoundError
# with open("non_existent_file.txt", "r") as file:
#     print(file.read())  # 文件不存在

# ImportError / ModuleNotFoundError
# import non_existent_module  # 模块不存在