import numpy as np
import pandas as pd

# 첫번째 컬럼을 인덱스로 country.csv 파일 읽어오기.
print("Country DataFrame")
country = pd.read_csv("./data/country.csv", index_col=0)
print(country, "\n")

# 명시적 인덱싱을 사용하여 데이터프레임의 "china" 인덱스를 출력해봅시다.
print(country.loc['china'])


# 정수 인덱싱을 사용하여 데이터프레임의 1번째부터 3번째 인덱스를 출력해봅시다.
print(country.iloc[1:4])
