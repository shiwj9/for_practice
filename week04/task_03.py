import time


def print_now_time():
    now_time = time.strftime(f'%Y-%m-%d %H:%M:%S', time.localtime())
    print("现在时间：", now_time)


def print_24h_later_time():
    current_time_seconds = time.time()
    twenty_four_hours_later_seconds = current_time_seconds + 24 * 3600

    # 将秒数转换回结构化时间
    twenty_four_hours_later = time.localtime(twenty_four_hours_later_seconds)
    formatted_future_time = time.strftime("%Y-%m-%d %H:%M:%S", twenty_four_hours_later)
    print("24小时后的时间:", formatted_future_time)


def count_for_time():
    start_time = time.perf_counter()

    for i in range(1000000):
        pass

    end_time = time.perf_counter()

    # 计算并打印执行时间，精确到小数点后五位
    for_time = end_time - start_time
    print(f"执行时间: {for_time:.5f} 秒")


print_now_time()
print_24h_later_time()
count_for_time()
