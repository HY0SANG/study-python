import numpy as np

print("array")  # array
array = np.arange(8)  # array([0, 1, 2, 3, 4, 5, 6, 7])
print(array)  # [0 1 2 3 4 5 6 7]
print("shape : ", array.shape, "\n")  # shape :  (8,)

# Q1. array를 (2,4) 크기로 reshape하여 matrix에 저장한 뒤 matrix와 그의 shape를 출력해보세요.
print("# reshape (2, 4)")  # # reshape (2, 4)
matrix = array.reshape(2, 4)  
matrix = np.reshape(array, (2, 4))
# array([[0, 1, 2, 3],
#        [4, 5, 6, 7]])

print(matrix)
# [[0 1 2 3]
# [4 5 6 7]]
print("shape : ", matrix.shape)
# shape :  (2, 4)
