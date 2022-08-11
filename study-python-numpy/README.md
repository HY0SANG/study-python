# Numpy Study
> ## 1. Numpy의 개요
>> ### 1.1 Numpy란?
>>> 1.1.1 **Numerical Python**의 약자
>>>
>>> 1.1.2 Python에서 **대규모 다차원 배열**을 다룰 수 있게 도와주는 라이브러리
>> ### 1.2 Numpy의 장점
>>> 1.2.1 Numpy는 List에 비해 **빠른 연산**을 지원하고 **메모리를 효율적**으로 사용
> ## 2. Numpy의 사용법
>> ### 2.1 Numpy import 방법 
>> Numpy는 관습적으로 **np**로 줄여씀
>>```python
>>import numpy as np
>>```
>> ### 2.2 Numpy 배열 만들기 [array]
>> Numpy의 배열은 아래와 같은 방법으로 만들 수 있다.
>>```python
>>np.array([1, 2, 3, 4, 5])
>># array([1, 2, 3, 4, 5])
>>
>>np.array([3, 1.4, 2, 3, 4])
>># array([3. , 1.4, 2. , 3. , 4. ])
>>
>>np.array([[1, 2],
>>          [3, 4]])
>># array([[1, 2],
>>         [3, 4]])
>>
>>np.array([1, 2, 3, 4], dtype='float')
>># array([1., 2., 3., 4.])
>>```
>> ### 2.3 Numpy의 다양한 배열 만들기
>> 아래와 같은 방법으로도 배열을 만들 수 있다.
>> ```python
>> np.zeros(10, dtype='int')
>> # array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
>>
>> np.ones((2, 4), dtype='float')
>> # array([[1., 1., 1., 1.],
>> #        [1., 1., 1., 1.]])
>>
>> np.arange(0, 20, 2)
>> # array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
>>
>> np.linspace(0, 1, 5)
>> array([0.  , 0.25, 0.5 , 0.75, 1.  ])
>> ```
>> ### 2.4 Numpy 배열 데이터 타입 [dtype]
>> Numpy의 배열은 List와 다르게 데이터 타입이 **단일 타입**으로 구성된다.
>>```python
>>arr = np.array([1, 2, 3, 4], dtype='float')
>>arr # array([1., 2., 3., 4.])
>>
>>arr.dtype
>># dtype('float64')
>>
>>arr.astype('int')
>># array([1, 2, 3, 4])
>>```
>>
>>> #### 2.4.1 dtype의 표현 방식
>>>
>>>|dtype|설명|표현 방식|
>>>|:---:|:---:|:---:|
>>>|int|정수형 타입|i, int_, int32, int64, i8|
>>>|float|실수형 타입|f, float_, float32, float64, f8|
>>>|str|문자열 타입|str, U, U32|
>>>|bool|부울 타입|?, bool_|
