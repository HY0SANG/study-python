import numpy as np

print("2차원 array")
matrix = np.arange(1, 16).reshape(3,5)  #1부터 15까지 들어있는 (3,5)짜리 배열을 만듭니다.
print(matrix)


# Q1. matrix의 자료형을 출력해보세요.
print(type(matrix))  # <class 'numpy.ndarray'>

# Q2. matrix의 차원을 출력해보세요.
print(matrix.ndim)  # 2

# Q3. matrix의 모양을 출력해보세요.
print(matrix.shape)  # (3, 5)

# Q4. matrix의 크기를 출력해보세요.
print(matrix.size)  # 15

# Q5. matrix의 dtype(data type)을 출력해보세요.
print(matrix.dtype)  # int64

# Q6. matrix의 (2,3) 인덱스의 요소를 출력해보세요.
print(matrix[2][3])  # 14

# Q7. matrix의 행은 인덱스 0부터 인덱스 1까지, 열은 인덱스 1부터 인덱스 3까지 출력해보세요.
print(matrix[0:2,1:4])  #[[2 3 4][7 8 9]]
