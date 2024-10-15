# 第一问
def apply_twice(func, val):
    val_01 = func(val)
    val_02 = func(val_01)
    return val_02


def a_function(val):
    return val * 2


result01 = apply_twice(a_function, 6)
print(f"第一问：{result01}")


# 第二问
def compose(f, g, x):
    x1 = g(x)
    x2 = f(x1)
    return x2


def func01(x):
    return x + 2


def func02(x):
    return x * 2


result02 = compose(func01, func02, 6)
print(f"第二问：{result02}")
