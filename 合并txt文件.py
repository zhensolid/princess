import os

# 将当前目录下的所有txt文件合并到一个文件

# key 获取当前目录下的文件列表
file_list = os.listdir()

# 创建一个新文件，用于保存合并后的内容
with open('result.txt', 'w') as f_result:
    # 遍历文件列表
    for filename in file_list:
        # 只处理txt文件
        if filename.endswith('.txt'):
            # 打开txt文件，读取内容
            with open(filename, 'r',encoding='UTF-8') as f_txt:
                content = f_txt.read()
                # 将读取的内容写入到result.txt文件中
                f_result.write(content)
                # 写入换行符
                f_result.write('\n')