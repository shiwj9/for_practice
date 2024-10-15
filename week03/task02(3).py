magicians_name = ["Lily", "Tom", "Sam"]


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


#  修改程序，在调用 make_great() 时传递魔术师列表的副本
def make_great(magicians):
    magicians_second_copy = magicians[:]
    for i in range(len(magicians_second_copy)):
        magicians_second_copy[i] = "the Great " + magicians_second_copy[i]
    return magicians_second_copy


# 创建魔术师列表的副本
magicians_copy = magicians_name[:]
# 调用函数，返回修改后的列表，并将其存储到另一个列表中
modified_magicians = make_great(magicians_copy)

print("原始魔术师列表:")
show_magicians(magicians_name)

print("修改后的魔术师列表:")
show_magicians(modified_magicians)
