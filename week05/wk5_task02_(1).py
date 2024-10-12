# 导入模块，用于数据处理和数学运算
import math


def process_data(file_name):
    # 读取文件，处理数据
    try:
        with open(file_name) as f:  # FileNotFoundError
            lines = f.readlines()
    except:
        print("File not found, continuing with default data.")
        lines = ["10", "20", "30", "invalid", "50"]

    data = []
    for line in lines:
        # 尝试将每一行转换为整数，如果失败则忽略
        try:
            num = int(line.strip())  # ValueError
            data.append(num)
        except:
            continue

    # 计算数据的总和和平均值
    total = sum(data)
    avg = total / len(data)  # 潜在ZeroDivisionError

    return data, total, avg


def calculate_area(radius, height=None):
    # 如果没有提供高度，默认为圆的面积；否则计算圆柱体积
    if height:
        area = math.pi * radius ** 2
        volume = area * height
        return volume
    else:
        area = math.pi * radius ** 2
        return area


def analyze_list(lst):
    try:
        # 访问列表中的元素，处理超出范围的索引
        return lst[10]  # IndexError
    except:
        return None


def manipulate_dict(d):
    try:
        # 访问字典中的键值
        return d["address"]  # KeyError (键不存在)
    except:
        d["address"] = "Unknown"
        return d["address"]


# 主函数执行流程
if __name__ == "__main__":
    # 调用数据处理函数
    file_data, total, avg = process_data("data.txt")

    # 基于处理数据，计算几何面积或体积
    try:
        result = calculate_area(file_data[0], file_data[1])
    except:
        result = calculate_area(file_data[0])

    # 分析列表并处理异常
    value = analyze_list(file_data)

    # 操作字典并处理异常
    info = {"name": "Alice", "age": 25}
    address = manipulate_dict(info)

    # 输出结果
    print(f"Processed Data: {file_data}")
    print(f"Total: {total}, Average: {avg}")
    print(f"Calculated Result: {result}")
    print(f"Value from List: {value}")
    print(f"Address: {address}")
