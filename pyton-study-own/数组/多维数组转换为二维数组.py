from tkinter.tix import COLUMN
import pandas as pd
import numpy as np


arr_A = np.random.rand(4,10,3)

print("四位数组")
print(arr_A)

# key 使用reshape函数整合数组
# 实例：np.reshape(arr_A,(-1,10))   -1代表不确定行数row，10对应列数col [数据均分]
# 实例：np.reshape(arr_A,(10,-1))   10代表确定行数row，-1不确定列数col [数据均分]
arr_B = np.reshape(arr_A,(-1,10))
print("整合二维数组")
print(arr_B)

arr_B_P = pd.DataFrame(arr_B)

arr_B_P.to_csv("四维数组整合二维.csv")
