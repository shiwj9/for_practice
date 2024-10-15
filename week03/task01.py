import os

# 创建content.txt文件
content_path = os.path.join(r'C:\Users\石温杰\Desktop', 'content.txt')
with open(content_path, 'w') as file:
    lines = ["the first line", "the second line", "the third line", "the forth line"]
    for line in lines:
        file.write(line + '\n')
# 读取文件内容
with open(content_path, 'r') as file:
    lines = file.readlines()

odd_lines = [line for index, line in enumerate(lines) if index % 2 == 0]  # 因为索引从0开始
total_lines = len(lines)
total_str = sum(len(line) for line in lines)

print("奇数行内容：")
for line in odd_lines:
    print(line.strip())

print(f"总行数：{total_lines}")
print(f"总字符数：{total_str}")

# 复制文件内容到copy_content.txt
copy_path = os.path.join(r'C:\Users\石温杰\Desktop', 'copy_content.txt')
with open(copy_path, 'w') as file:
    file.writelines(lines)

# 创建文件夹
folder_path = os.path.join(r'C:\Users\石温杰\Desktop', 'txt.files')
os.makedirs(folder_path, exist_ok=True)

# 在文件夹中创建100个.txt文件
for i in range(1, 101):
    file_name = f"file{i}.txt"
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as file:
        pass  # 创建空文件

# 将所有.txt文件重命名为.jpg
for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        old_file_path = os.path.join(folder_path, file_name)
        new_file_name = file_name[:-4] + '.jpg'
        new_file_path = os.path.join(folder_path, new_file_name)
        os.rename(old_file_path, new_file_path)


def count(path):
    file_count = 0
    folder_count = 0
    for root, dirs, files in os.walk(path):
        file_count += len(files)
        folder_count += len(dirs)
    return file_count, folder_count


desktop_path = r'C:\Users\石温杰\Desktop'
files_count, folders_count = count(desktop_path)
print(f"文件数量：{files_count}")
print(f"文件夹数量：{folders_count}")
