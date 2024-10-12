import random
import string

digits = string.digits
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

# 生成至少一个数字，一个大写字母，一个小写字母
the_digit = random.choice(digits)
the_lowercase = random.choice(lowercase)
the_uppercase = random.choice(uppercase)

# 将这三个字符放入一个列表中
chars_list = [the_digit, the_lowercase, the_uppercase]

# 生成剩余字符
all_chars = digits + lowercase + uppercase
the_rest_of_chars = random.sample(all_chars, 3)  # 这将返回3个不重复的随机字符

# 将所有字符放入一个列表中
code_list = chars_list + the_rest_of_chars

# 打乱顺序
random.shuffle(code_list)

# 转换为字符串并输出
code = ''.join(code_list)
print(f'验证码：{code}')
