# key 导入模块
import numpy as np
import pandas as pd
import random

# key 创建10行的随机名称，取5个字母
random_cow = []
for i in range(10):
    random_cow.append(''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5)))

# key 创建3列的随机名称，取3个字母
random_col = []
for i in range(3):
    random_col.append(''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3)))

# key 使用numpy创建10行3列的随机数据
arry_10x3 = np.random.rand(10,3)

# key 使用dataframe导入数据和行和列名称
arr_a = pd.DataFrame(arry_10x3,index=random_cow,columns=random_col)

print(arr_a)

# key 导入到csv
arr_a.to_csv("D:\Github\QTYX\随机一维数组.csv")