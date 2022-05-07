
# ! 帮助你将Excel工作表sheet合并到一张表上,
# ! 6张表，其余表的内容和第一张表都一样
# ! 设置表格数量为5，将会合并前5张表的内容

import pandas as pd

# 文件名
filename = "test.xlsx"
# 表格数量
T_sheets = 5

df = []
for i in range(1, T_sheets+1):
    sheet_data = pd.read_excel(filename, sheet_name=i, header=None)
    df.append(sheet_data)

# 合并表格
output = "merged.xlsx"
df = pd.concat(df)
df.to_excel(output)
