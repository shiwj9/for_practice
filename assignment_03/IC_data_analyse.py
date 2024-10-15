import numpy as np
import pandas as pd
import os

data = pd.read_csv("ICData.csv",dtype={'驾驶员编号': int})

# 1. 分别计算早上7点前和晚上10点之后的公共交通上车刷卡量
# 将交易时间转换为datetime类型
data['交易时间'] = pd.to_datetime(data['交易时间'])

# 计算早上7点前的刷卡量
before_7am = data[data['交易时间'].dt.hour < 7]['交易卡号'].count()

# 计算晚上10点之后的刷卡量
after_10pm = data[data['交易时间'].dt.hour >= 22]['交易卡号'].count()

print("要求1：")
print(f"早上7点前的刷卡量: {before_7am}")
print(f"晚上10点之后的刷卡量: {after_10pm}")

# 2. 构造一个乘客搭乘站点数分析函数，计算不同线路乘客的平均公交搭乘站点数及其标准差
# 计算搭乘站点数，形成新的的一列
data['搭乘站点数'] = abs(data['下车站点'] - data['上车站点']) + 1  # 加1是因为包含起点和终点


# 计算不同线路乘客的平均公交搭乘站点数及其标准差
def calculate_average_stations(data):
    grouped = data.groupby('线路号')
    averages = grouped['搭乘站点数'].mean()
    std_devs = grouped['搭乘站点数'].std()
    return averages, std_devs


averages, std_devs = calculate_average_stations(data)
print("要求2：")
print("不同线路乘客的平均公交搭乘站点数:")
print(averages)
print("不同线路公交搭乘站点数的标准差:")
print(std_devs)

# 3. 计算高峰小时刷卡量和公交刷卡量的高峰小时系数（PHF5和PHF15）
# 新建一列表示小时
data['小时'] = [x.hour for x in data['交易时间']]
# 按小时划分出刷卡量（新的DataFrame）
data_hour = data[['小时', '交易卡号']].groupby('小时', as_index=False).count().rename(columns={'交易卡号': '刷卡量'})
# 高峰小时索引
index = data_hour['刷卡量'].idxmax(axis=0, skipna=True)
# 高峰小时
peak_hour = data_hour['小时'][index]
# 高峰小时刷卡量
peak_hour_volume = data_hour['刷卡量'].max()
print(f"高峰小时({peak_hour}点)刷卡量：{peak_hour_volume}")


def calculate_phf(data, peak_hour):
    # 高峰小时的开始（peak_hour转换为 timedelta 对象）
    peak_start = pd.Timestamp('2018-04-01') + pd.to_timedelta(peak_hour, unit='h')

    # peak_end = peak_start + pd.Timedelta(hours=1)

    # 根据时间间隔计算高峰小时系数
    def peak_volume_in_interval(interval_minutes):
        # 高峰小时按特定间隔分割成区间
        intervals = [(peak_start + pd.Timedelta(minutes=i * interval_minutes),
                      peak_start + pd.Timedelta(minutes=(i + 1) * interval_minutes)) for i in
                     range(int(60 / interval_minutes))]
        # 高峰区间流量
        peak_intervals_volume = [data[(data['交易时间'] >= start) & (data['交易时间'] < end)]['交易卡号'].count()
                                 for start, end in intervals]
        return max(peak_intervals_volume)

    # 计算高峰小时系数
    phf5 = peak_hour_volume / (12 * peak_volume_in_interval(5))
    phf15 = peak_hour_volume / (4 * peak_volume_in_interval(15))

    return phf5, phf15


phf5, phf15 = calculate_phf(data, peak_hour)
print(f"PHF5约为: {round(phf5, 3)}")
print(f"PHF15约为: {round(phf15, 3)}")

# 4. 输出线路号1101-1120中各个车辆编号对应的的驾驶员编号，分别输出为20个txt文档
# 筛选线路号1101-1120的数据
filtered_data = data[(data['线路号'] >= 1101) & (data['线路号'] <= 1120)]

# 新建文件夹
if not os.path.exists("line_1101-1120"):
    os.makedirs("line_1101-1120")

# 为每个线路号创建一个txt文件，并写入相应的数据
for line_no in range(1101, 1121):
    line_data = filtered_data[filtered_data['线路号'] == line_no]

    # 如果该线路没有数据，则跳过
    if line_data.empty:
        continue

        # 文件名
    file_path = os.path.join("line_1101-1120", f"line_{line_no}.txt")

    # 打开文件准备写入
    with open(file_path, 'w') as file:
        # 遍历每个车辆编号及其对应的组
        # vehicle_id被赋值为当前分组的 '车辆编号'， group 被赋值为包含该车辆编号所有相关行的DataFrame
        for vehicle_id, group in line_data.groupby('车辆编号'):
            driver_ids = group['驾驶员编号'].unique()
            # 写入车辆编号和对应的驾驶员编号
            file.write(f"车辆编号: {vehicle_id}\n")
            for driver_id in driver_ids:
                file.write(f"  驾驶员编号: {driver_id}\n")
            # 添加一个空行作为分隔
            file.write("\n")


# 5. 分析搭载乘客情况，确定服务乘客人次最多的10个司机、10条线路、10个站点和10台车辆
def top_n_analysis(data, n=10):
    driver_counts = data.groupby('驾驶员编号')['交易卡号'].count().rename('服务乘客人次').sort_values(ascending=False).head(n)
    line_counts = data.groupby('线路号')['交易卡号'].count().rename('服务乘客人次').sort_values(ascending=False).head(n)
    stop_counts = data.groupby('上车站点')['交易卡号'].count().rename('服务乘客人次').sort_values(ascending=False).head(n)
    vehicle_counts = data.groupby('车辆编号')['交易卡号'].count().rename('服务乘客人次').sort_values(ascending=False).head(n)

    print("服务乘客人次最多的10个司机:")
    print(driver_counts)
    print("\n服务乘客人次最多的10条线路:")
    print(line_counts)
    print("\n服务乘客人次最多的10个站点:")
    print(stop_counts)
    print("\n服务乘客人次最多的10台车辆:")
    print(vehicle_counts)


top_n_analysis(data)
