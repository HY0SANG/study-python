import numpy as np

print("1차원 array")  # 1차원 array
array = np.arange(10)
print(array)
# [0 1 2 3 4 5 6 7 8 9]

# Q1. array의 자료형을 출력해보세요.
print(type(array))  # <class 'numpy.ndarray'>

# Q2. array의 차원을 출력해보세요.
print(array.ndim)  # 1

# Q3. array의 모양을 출력해보세요.
print(array.shape)  #(10,)

# Q4. array의 크기를 출력해보세요.
print(array.size)  # 10

# Q5. array의 dtype(data type)을 출력해보세요.
print(array.dtype)  # int32

# Q6. array의 인덱스 5의 요소를 출력해보세요.
print(array[5])  # 5

# Q7. array의 인덱스 3의 요소부터 인덱스 5 요소까지 출력해보세요.
print(array[3:6])  # [3 4 5]
