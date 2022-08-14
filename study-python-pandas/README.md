# Pandas Study
> ## 1. Pandas의 개요
>> ### 1.1 Pandas란?
>> Pandas는 구조화된 데이터를 효과적으로 처리하고 저장할 수 있는 라이브러리이다.
>> 
>> 또한, Array 계산에 특화된 Numpy를 기반으로 만들어져 다양한 기능들을 제공한다.
>
>
>
> ## 2. Pandas의 사용법
>> ### 2.1 Pandas import 방법 
>> Pandas는 관습적으로 **pd**로 줄여씀
>>```python
>>import pandas as pd
>>```
>
>
>
> ## 3. Pandas의 데이터 형태
>> ### 3.1 Pandas의 Series
>> Series는 Numpy의 ndarray가 보강된 형태의 데이터로 Index를 가지고 있다.
>> ```python 
>> data = pd.Series([1, 2, 3, 4])
>> # 0    1
>> # 1    2
>> # 2    3
>> # 3    4
>> # dtype: int64
>> 
>> data = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
>> # a    1
>> # b    2
>> # c    3
>> # d    4
>> # dtype: int64
>> 
>> data['b']  # 2
>> ```
>>
>> 딕셔너리를 이용하여 Series 데이터로 만들 수 있다.
>> ```python
>> population_dict = {
>>     'korea': 5180,
>>     'japan': 12718,
>>     'china': 141500,
>>     'usa': 32676
>> }
>> # {'korea': 5180, 'japan': 12718, 'china': 141500, 'usa': 32676} 
>>
>> population = pd.Series(population_dict)
>> # korea      5180
>> # japan     12718
>> # china    141500
>> # usa       32676
>> # dtype: int64
>>
>> population.values  # array([  5180,  12718, 141500,  32676], dtype=int64)
>> ```
>>
>>
>> ### 3.2 Pandas의 DataFrame
>> DataFrame은 여러 개의 Series 데이터가 모여 **행(Index)** 과 **열(Columns)** 을 이룬다.
>> ```python
>> population_dict = {
>>     'korea': 5180,
>>     'japan': 12718,
>>     'china': 141500,
>>     'usa': 32676
>> }
>> # {'korea': 5180, 'japan': 12718, 'china': 141500, 'usa': 32676} 
>> 
>> gdp_dict = {
>>     'korea': 169320000,
>>     'japan': 516700000,
>>     'china': 1409250000,
>>     'usa': 2041280000
>> }
>> # {'korea': 169320000, 'japan': 516700000,
>> #  'china': 1409250000, 'usa': 2041280000}
>> 
>> population = pd.Series(population_dict)
>> # korea      5180
>> # japan     12718
>> # china    141500
>> # usa       32676
>> # dtype: int64
>> 
>> gdp = pd.Series(gdp_dict)
>> # korea     169320000
>> # japan     516700000
>> # china    1409250000
>> # usa      2041280000
>> # dtype: int64
>> 
>> country = pd.DataFrame({
>>     'population': population,
>>     'gdp': gdp
>> })
>> #        population         gdp
>> # korea        5180   169320000
>> # japan       12718   516700000
>> # china      141500  1409250000
>> # usa         32676  2041280000
>>
>> country.index  # Index(['korea', 'japan', 'china', 'usa'], dtype='object')
>> country.columns  # Index(['population', 'gdp'], dtype='object')
>> 
>> country['gdp']
>> # korea     169320000
>> # japan     516700000
>> # china    1409250000
>> # usa      2041280000
>> # Name: gdp, dtype: int64\
>> 
>> country['gdp']['korea']  # 169320000
>> ```
>> 
>
>
>
> ## 4. Pandas DataFrame의 연산
> **country** DataFrame의 값은 <a href="https://github.com/HY0SANG/study-python/blob/main/study-python-pandas/README.md#32-pandas%EC%9D%98-dataframe">3.2 Pandas의 DataFrame</a> 참고
> ```python
> gdp_per_capita = country['gdp'] / country['population']
> # korea    32687.258687
> # japan    40627.457147
> # china     9959.363958
> # usa      62470.314604
> # dtype: float64
> 
> country['gdp per capita'] = gdp_per_capita
> #        population         gdp  gdp per capita
> # korea        5180   169320000    32687.258687
> # japan       12718   516700000    40627.457147
> # china      141500  1409250000     9959.363958
> # usa         32676  2041280000    62470.314604
> ```
> 
>
>
>
> ## 5. Pandas DataFrame의 저장과 불러오기
>> ### 5.1 Pandas DataFrame의 저장 [to_?]
>> ```python
>> country.to_csv("./country.csv")
>> country.to_excel("./country.xlsx")
>> ```
>> 
>> ### 5.2 Pandas DataFrame의 저장 [read_?]
>> ```python
>> country = pd.read_csv("./country.csv")
>> country = pd.read_excel("./country.xlsx")
>> ```
>
>
>
> ## 6. Pandas DataFrame의 인덱싱과 슬라이싱
>> ### 6.1 Pandas DataFrame의 인덱싱 [Indexing]
>> ```python
>> country.loc['china']  # == country.iloc[2]
>> # population        1.415000e+05
>> # gdp               1.409250e+09
>> # gdp per capita    9.959364e+03
>> # Name: china, dtype: float64
>> 
>> ```
>>
>>
>> ### 6.2 Pandas DataFrame의 슬라이싱 [Slicing]
>> ```python
>> country.loc['korea':'japan']  # == country.iloc[0:2, :1]
>> #        population
>> # korea        5180
>> # japan       12718
>> 
>> ```
>>
>>
>> ### 6.3 Pandas DataFrame의 인덱싱과 슬라이싱을 사용하여 데이터 추가 및 선택
>> ```python
>> df = pd.DataFrame(columns=['이름', '나이', '주소'])
>> df.loc[0] = ['김효상', '24', '한국']
>> #     이름  나이  주소
>> # 0  김효상  24  한국
>> 
>> df.loc[1] = {'이름':'둘효상', '나이':'25', '주소':'미국'}
>> #     이름  나이  주소
>> # 0  김효상  24  한국
>> # 1  둘효상  25  미국
>> 
>> df.loc[1, '이름'] = '셋효상'
>> #     이름  나이  주소
>> # 0  김효상  24  한국
>> # 1  셋효상  25  미국
>> 
>> df['전화번호'] = np.nan
>> #     이름  나이  주소  전화번호
>> # 0  김효상  24  한국   NaN
>> # 1  셋효상  25  미국   NaN
>> 
>> df.loc[0, '전화번호'] = '01012341234'
>> #     이름  나이  주소     전화번호
>> # 0  김효상  24  한국  01012341234
>> # 1  셋효상  25  미국          NaN
>>
>> # 컬럼 이름이 하나만 있으면 Series로 반환
>> df['이름']
>> # 0    김효상
>> # 1    셋효상
>> # Name: 이름, dtype: object
>> 
>> # 컬럼 이름이 리스트로 있으면 DataFrame으로 반환
>> df[['이름', '주소']]
>> #      이름  주소
>> # 0  김효상  한국
>> # 1  셋효상  미국
>> ```
