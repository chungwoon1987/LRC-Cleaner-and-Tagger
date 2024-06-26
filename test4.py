import os

# 设置文件夹路径
directory_path = 'D:\\lrc (2)'

# 删除ZWNBSP字符的函数
def remove_zwnbsp(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('\uFEFF', '')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# 插入[ti]和[ar]标签的函数
def insert_ti_ar(file_path, A, B):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 如果第一行没有[ti]，则插入[ti]和[ar]
    if not any(line.startswith('[ti') for line in lines):
        lines.insert(0, f'[ti:{B}]\n')
        lines.insert(1, f'[ar:{A}]\n')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)

# 遍历文件夹中的所有.lrc文件
for filename in os.listdir(directory_path):
    if filename.endswith('.lrc'):
        parts = filename.split(' - ')
        if len(parts) == 2:
            # 分割文件名，移除扩展名
            A, B = parts[0], parts[1].replace('.lrc', '')
            file_path = os.path.join(directory_path, filename)
            # 先删除ZWNBSP字符
            remove_zwnbsp(file_path)
            # 然后插入[ti]和[ar]标签
            insert_ti_ar(file_path, A, B)

print("所有.lrc文件已检查并更新。")


# 这个脚本首先定义了两个函数：
# `remove_zwnbsp` 用于删除ZWNBSP字符，
# `insert_ti_ar` 用于插入`[ti]`和`[ar]`标签。
# 然后，它会遍历指定文件夹中的所有`.lrc`文件，
# 先调用 `remove_zwnbsp` 函数删除ZWNBSP字符，
# 再调用 `insert_ti_ar` 函数检查并插入标签。
