import numpy as np

matrix = np.arange(8).reshape((2, 4))
print(matrix)
# [[0 1 2 3]
#  [4 5 6 7]]

# Q1. 마스킹 연산을 이용하여 matrix 중 5보다 작은 수들만 추출하여 출력해보세요.
print(matrix[matrix < 5])  # [0 1 2 3 4]
