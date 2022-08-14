import numpy as np

matrix = np.arange(8).reshape((2, 4))
print(matrix)
# [[0 1 2 3]
#  [4 5 6 7]]

# Q1. sum 함수로 matrix의 총 합계를 구해 출력해보세요.
print(np.sum(matrix))  # 28

# Q2. max 함수로 matrix 중 최댓값을 구해 출력해보세요.
print(np.max(matrix))  # 7

# Q3. min 함수로 matrix 중 최솟값을 구해 출력해보세요.
print(np.min(matrix))  # 0

# Q4. mean 함수로 matrix의 평균값을 구해 출력해보세요.
print(np.mean(matrix))  # 3.5

# Q5. sum 함수의 axis 매개변수로 각 열의 합을 구해 출력해보세요.
print(np.sum(matrix, axis=0))  # [ 4  6  8 10]

# Q6. sum 함수의 axis 매개변수로 각 행의 합을 구해 출력해보세요.
print(np.sum(matrix, axis=1))  # [ 6 22]

# Q7. std 함수로 matrix의 표준편차를 구해 출력해보세요.
print(np.std(matrix))  # 2.29128784747792

# Q8. 마스킹 연산을 이용하여 matrix 중 5보다 작은 수들만 추출하여 출력해보세요.
print(matrix[matrix < 5])  # [0 1 2 3 4]
