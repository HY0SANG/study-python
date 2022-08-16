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
