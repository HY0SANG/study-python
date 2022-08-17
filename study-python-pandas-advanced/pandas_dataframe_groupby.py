import numpy as np
import pandas as pd

df = pd.DataFrame({
    'key': ['A', 'B', 'C', 'A', 'B', 'C'],
    'data1': [1, 2, 3, 1, 2, 3],
    'data2': [4, 4, 6, 0, 6, 1]
})
print("DataFrame:")
print(df, "\n")

# groupby 함수를 이용해봅시다.
# key를 기준으로 묶어 합계를 구해 출력해보세요.
print(df.groupby('key').sum())


# key와 data1을 기준으로 묶어 합계를 구해 출력해보세요.
print(df.groupby(['key', 'data1']).sum())


# aggregate를 이용하여 요약 통계량을 산출해봅시다.
# 데이터 프레임을 'key' 칼럼으로 묶고, data1과 data2 각각의 최솟값, 중앙값, 최댓값을 출력하세요.
print(df.groupby('key').aggregate([min, np.mean, max]))


# 데이터 프레임을 'key' 칼럼으로 묶고, data1의 최솟값, data2의 합계를 출력하세요.
print(df.groupby('key').aggregate({'data1': min, 'data2': sum}))




df = pd.DataFrame({
    'key': ['A', 'B', 'C', 'A', 'B', 'C'],
    'data1': [0, 1, 2, 3, 4, 5],
    'data2': [4, 4, 6, 0, 6, 1]
})
print("DataFrame:")
print(df, "\n")

# groupby()로 묶은 데이터에 filter를 적용해봅시다.
# key별 data2의 평균이 3이 넘는 인덱스만 출력해봅시다.
def filter_by_mean(x):
    return x['data2'].mean() > 3

print("filtering : ")
print(df.groupby('key').filter(filter_by_mean))


# groupby()로 묶은 데이터에 apply도 적용해봅시다.
# 람다식을 이용해 최댓값에서 최솟값을 뺀 값을 적용해봅시다.

print("applying : ")
print(df.groupby('key').apply(lambda x: x.max() - x.min()))
