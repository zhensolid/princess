
import numpy as np
array_4x3a = np.array([[1,2,3,4],[1,2,3,4]])
array_4x3b = np.array([[1,2,3,4],[1,2,3,4]])
array_4x3c = np.array([[0,0,0,0],[0,0,0,0]])

for i in range(2):      # key 代表几组数组
    for j in range(4):  # key 代表几组数据
        array_4x3c[i][j] = array_4x3a[i][j] + array_4x3b[i][j]
        
print (array_4x3c)