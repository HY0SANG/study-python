import numpy as np
import pandas as pd

df1 = pd.DataFrame(
    np.random.randn(4, 2), 
    index=[['A', 'A', 'B', 'B'], [1, 2, 1, 2]],
    columns=['data1', 'data2']
)
print("DataFrame1")
print(df1, "\n")

df2 = pd.DataFrame(
    np.random.randn(4, 4),
    columns=[["A", "A", "B", "B"], ["1", "2", "1", "2"]]
)
print("DataFrame2")
print(df2, "\n")

# 명시적 인덱싱을 활용한 df1의 인덱스 출력
print("df1.loc['A', 1]")
print(df1.loc['A', 1], "\n")


# df2의 [A][1] 칼럼 출력
print('df2["A"]["1"]')
print(df2["A"]["1"], "\n")
