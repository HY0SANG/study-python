import numpy as np
import pandas as pd


print("A: ")
A = pd.DataFrame(np.random.randint(0, 10, (2, 2)), columns=['A', 'B'])      #칼럼이 A, B입니다.
print(A, "\n")


print("B: ")
B = pd.DataFrame(np.random.randint(0, 10, (3, 3)), columns=['B', 'A', 'C'])     #칼럼이 B, A, C입니다.
print(B, "\n")


# 아래에 다양한 연산을 자유롭게 적용해보세요.
print("A + B: ")
print(A + B, "\n")

print("A.add(B, fill_value=0): ")
print(A.add(B, fill_value=0), "\n")

print("A.sum(): ")
print(A.sum(), "\n")

print("A['A'].sum(): ")
print(A['A'].sum(), "\n")
