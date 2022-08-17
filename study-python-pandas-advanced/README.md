# Pandas Advanced Study
> ## 1. Pandas DataFrame의 조건으로 검색하기
> ```python
> df = pd.DataFrame(np.random.rand(5, 2), columns=["A", "B"])
> #           A         B
> # 0  0.094758  0.736905
> # 1  0.888602  0.677492
> # 2  0.354974  0.317544
> # 3  0.812493  0.180605
> # 4  0.343886  0.686311 
> 
> # 마스킹 연산을 사용하여 검색하기
> print(df[(df["A"] < 0.5) & (df["B"] > 0.3)])
> # query 함수를 사용하여 검색하기
> print(df.query("A < 0.5 and B > 0.3"))
>
> # 결과 값
> #           A         B
> # 0  0.094758  0.736905
> # 2  0.354974  0.317544
> # 4  0.343886  0.686311
> ```
>
>
>
> ## 2. Pandas DataFrame의 함수로 데이터 처리하기
>> ### 2.1 DataFrame에 apply를 이용하여 함수 적용하기
>> ```python
>> df = pd.DataFrame(np.arange(5), columns=["Num"])
>> #    Num
>> # 0    0
>> # 1    1
>> # 2    2
>> # 3    3
>> # 4    4
>>
>> # x를 제곱하여 반환하는 함수
>> def square(x):
>>     return x**2
>> 
>> df["Num"].apply(square)
>> # 0     0
>> # 1     1
>> # 2     4
>> # 3     9
>> # 4    16
>> # Name: Num, dtype: int64
>> ```
>>
>>
>> ### 2.2 DataFrame에 lambda식을 이용하여 함수 적용하기
>> ```python
>> df["Num"].apply(lambda x: x ** 2)
>> # 0     0
>> # 1     1
>> # 2     4
>> # 3     9
>> # 4    16
>> # Name: Num, dtype: int64
>> ```
>
>
>
> ## 3. Pandas DataFrame을 그룹으로 묶기
>> ### 3.1 DataFrame에 groupby를 이용하여 그룹으로 묶고 집계
>> ```python
>> df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
>>                    'data1': [1, 2, 3, 1, 2, 3],
>>                    'data2': np.random.randint(0, 6, 6)})
>> #   key  data1  data2
>> # 0   A      1      5
>> # 1   B      2      0
>> # 2   C      3      5
>> # 3   A      1      1
>> # 4   B      2      5
>> # 5   C      3      5
>>
>> df.groupby('key').sum()
>> #      data1  data2
>> # key              
>> # A        2      6
>> # B        4      5
>> # C        6     10
>>
>> df.groupby(['key', 'data2']).sum()
>> #            data1
>> # key data2       
>> # A   1          1
>> #     5          1
>> # B   0          2
>> #     5          2
>> # C   5          6
>> ```
>>
>>
>> ### 3.2 그룹으로 묶인 DataFrame에 aggregate를 이용하여 한번에 집계
>> ```python
>> df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
>>                    'data1': [1, 2, 3, 1, 2, 3],
>>                    'data2': np.random.randint(0, 6, 6)})
>> #   key  data1  data2
>> # 0   A      1      3
>> # 1   B      2      1
>> # 2   C      3      0
>> # 3   A      1      0
>> # 4   B      2      4
>> # 5   C      3      4
>> 
>> print(df.groupby('key').aggregate(['min', np.median, max]))
>> #     data1            data2           
>> #       min median max   min median max
>> # key                                  
>> # A       1    1.0   1     0    1.5   3
>> # B       2    2.0   2     1    2.5   4
>> # C       3    3.0   3     0    2.0   4
>> 
>> print(df.groupby('key').aggregate({'data1':min, 'data2': np.sum}))
>> #      data1  data2
>> # key              
>> # A        1      3
>> # B        2      5
>> # C        3      4
>> ```
>>
>>
>> ### 3.3 그룹으로 묶인 DataFrame에 filter를 이용하여 데이터 필터링
>> ```python
>> df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
>>                     'data1': [0, 1, 2, 3, 4, 5],
>>                     'data2': np.random.randint(0, 6, 6)})
>> #   key  data1  data2
>> # 0   A      0      2
>> # 1   B      1      0
>> # 2   C      2      4
>> # 3   A      3      5
>> # 4   B      4      4
>> # 5   C      5      4
>> 
>> def filter_by_mean(x):
>>     return x['data2'].mean() > 3
>> 
>> df.groupby('key').filter(filter_by_mean)
>> #   key  data1  data2
>> # 0   A      0      2
>> # 2   C      2      4
>> # 3   A      3      5
>> # 5   C      5      4
>> ```
>>
>>
>> ## 3.3 그룹으로 묶인 DataFrame에 apply를 이용하여 함수 적용
>> ```python
>> df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
>>                     'data1': [0, 1, 2, 3, 4, 5],
>>                     'data2': np.random.randint(0, 6, 6)})
>> #   key  data1  data2
>> # 0   A      0      5
>> # 1   B      1      1
>> # 2   C      2      5
>> # 3   A      3      3
>> # 4   B      4      0
>> # 5   C      5      0
>> 
>> df.groupby('key').apply(lambda x: x.max() - x.min())
>> #      data1  data2
>> # key              
>> # A        3      2
>> # B        3      1
>> # C        3      5
>> ```
>>
>>
>> ## 3.4 그룹으로 묶인 DataFrame에 get_group을 이용하여 묶인 데이터에서 key값으로 데이터 가져오기
>> ```python
>> df = pd.DataFrame({
>>         "animal": "cat dog cat fish dog cat cat".split(),
>>         "size": list("SSMMMLL"),
>>         "weight": [8, 10, 11, 1, 20, 12, 12],
>>         "adult": [False] * 5 + [True] * 2,
>> })
>> #   animal size  weight  adult
>> # 0    cat    S       8  False
>> # 1    dog    S      10  False
>> # 2    cat    M      11  False
>> # 3   fish    M       1  False
>> # 4    dog    M      20  False
>> # 5    cat    L      12   True
>> # 6    cat    L      12   True
>> 
>> df.groupby(["animal"]).get_group("cat")
>> #   animal size  weight  adult
>> # 0    cat    S       8  False
>> # 2    cat    M      11  False
>> # 5    cat    L      12   True
>> # 6    cat    L      12   True
>> ```
