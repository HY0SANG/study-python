import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(5), columns=["Num"])
print(df, "\n")

# 값을 받으면 제곱을 해서 돌려주는 함수
def square(x):
    return x ** 2


# apply로 컬럼에 함수 적용
df["Square"] = df["Num"].apply(square)


# 람다 표현식으로도 적용하기
df["Square"] = df["Num"].apply(lambda x: x ** 2)
print(df)
