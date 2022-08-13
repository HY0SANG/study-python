import numpy as np

array = np.array([1,2,3,4,5])
print(array)  # [1 2 3 4 5]


# Q1. array에 5를 더한 값을 출력해보세요.
print(array + 5)  # [ 6  7  8  9 10]

# Q2. array에 5를 뺀 값을 출력해보세요.
print(array - 5)  # [-4 -3 -2 -1  0]

# Q3. array에 5를 곱한 값을 출력해보세요.
print(array * 5)  # [ 5 10 15 20 25]

# Q4. array를 5로 나눈 값을 출력해보세요.
print(array / 5)  # [0.2 0.4 0.6 0.8 1. ]


# Q5. array에 array2를 더한 값을 출력해보세요.    
array2 = np.array([5,4,3,2,1])
print(array + array2)  # [6 6 6 6 6]


# Q6. array에 array2를 뺀 값을 출력해보세요.
print(array - array2)  # [-4 -2  0  2  4]
