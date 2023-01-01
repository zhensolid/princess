from array import array
import numpy as np
import pandas as pd

arr_2x10x3 = np.random.randn(3,10,3)

arr_A = np.reshape(arr_2x10x3,(5,-1))

arr_B = pd.DataFrame(arr_A)

print(arr_B)

# arr_B.to_csv("filename2.csv")