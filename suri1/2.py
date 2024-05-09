#連立n次方程式 n=2とする。
import numpy as np

A = np.array([[2, 1], [1, 3]])

B = np.array([4, 2])

# 連立一次方程式を解く
X = np.linalg.solve(A, B)

print("解は:", X)


