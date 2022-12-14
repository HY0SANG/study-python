# Numpy Study
> ## 1. Numpy의 개요
>> ### 1.1 Numpy란?
>>> 1.1.1 **Numerical Python**의 약자
>>>
>>> 1.1.2 Python에서 **대규모 다차원 배열**을 다룰 수 있게 도와주는 라이브러리
>> ### 1.2 Numpy의 장점
>>> 1.2.1 Numpy는 List에 비해 **빠른 연산**을 지원하고 **메모리를 효율적**으로 사용
>
>
>
> ## 2. Numpy의 사용법
>> ### 2.1 Numpy import 방법 
>> Numpy는 관습적으로 **np**로 줄여씀
>>```python
>>import numpy as np
>>```
>
>
>
> ## 3. Numpy의 배열 생성 방법
>> ### 3.1 Numpy array 함수를 사용한 배열 생성 방법
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
>>> #### 3.1.1 array 함수의 매개변수
>>> ```python
>>>np.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)
>>>```
>>>|Parameter|Type|Optional|
>>>|:--:|:--:|:--:|
>>>|object|array_like|N|
>>>|dtype|data-type|Y|
>>>|copy|bool|Y|
>>>|order|{'K','A','C','F'}|Y|
>>>|subok|bool|Y|
>>>|ndmin|int|Y|
>>>|like|array_like|Y|
>>
>>
>> ### 3.2 Numpy의 다양한 배열 만들기 [zeros, ones, arange, linspace]
>> 아래와 같은 방법으로도 배열을 만들 수 있다.
>> ```python
>> np.zeros(10, dtype='int')
>> # array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
>>
>> np.ones((2, 4), dtype='float')
>> # array([[1., 1., 1., 1.],
>> #        [1., 1., 1., 1.]])
>>
>> np.arange(6)
>> # array([0, 1, 2, 3, 4, 5])
>>
>> np.arange(0, 20, 2)
>> # array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
>>
>> np.linspace(0, 1, 5)
>> # array([0.  , 0.25, 0.5 , 0.75, 1.  ])
>> ```
>>
>>
>> ### 3.3 Numpy의 난수로 채워진 배열 만들기 [random, normal, randint] <a href='https://github.com/HY0SANG/study-python/blob/main/study-python-numpy/random.py'><image width='23px' src='https://user-images.githubusercontent.com/110414297/184264138-d62cb488-d3f1-45c6-9f4e-d48b93aefabf.png'></a>
>> 아래와 같은 방법으로 난수로 채워진 배열을 만들 수 있다.
>> ```python
>> np.random.random((2, 2))
>> # array([[0.1246479 , 0.43909669],
>> #        [0.58342935, 0.2280941 ]])
>>
>> np.random.normal(0, 1, (2,2))
>> # array([[ 1.23267107,  0.37128397],
>> #        [ 0.91725704, -0.56180164]])
>> 
>> np.random.randint(0, 10, (2, 2))
>> # array([[0, 3],
>> #        [7, 5]])
>> ```
>>
>>
>>
>> ## 4. Numpy 배열의 속성
>> ### 4.1 Numpy 배열의 데이터 타입 [dtype]
>> Numpy 배열은 List와 다르게 데이터 타입이 **단일 타입**으로 구성된다.
>>
>> 배열의 데이터 타입은 `arr.dtype` 으로 확인할 수 있다.
>>```python
>> arr = np.array([1, 2, 3, 4], dtype='float')
>> arr # array([1., 2., 3., 4.])
>>
>> arr.dtype
>> # dtype('float64')
>>
>> arr.astype('int')
>> # array([1, 2, 3, 4])
>>```
>>> #### 4.1.1 dtype의 표현 방식
>>>|dtype|설명|표현 방식|
>>>|:---:|:---:|:---:|
>>>|int|정수형 타입|i, int_, int32, int64, i8|
>>>|float|실수형 타입|f, float_, float32, float64, f8|
>>>|str|문자열 타입|str, U, U32|
>>>|bool|부울 타입|?, bool_|
>>
>>
>> ### 4.2 Numpy 배열의 차원 [ndim]
>> 배열의 차원은 `arr.ndim` 으로 확인할 수 있다.
>>```python
>> np.array([1, 2, 3, 4]).ndim  # 1
>>
>> np.array([[1, 2], [3, 4]]).ndim  # 2
>>```
>>
>>
>> ### 4.3 Numpy 배열의 모양 [shape]
>> 배열의 모양은 `arr.shape` 로 확인할 수 있다.
>>```python
>> np.array([1, 2, 3, 4]).shape  # (4,)
>>
>> np.array([[1, 2], [3, 4]]).shape  # (2, 2)
>>```
>>
>>
>> ### 4.4 Numpy 배열의 크기 [size]
>> 배열의 크기는 `arr.size` 로 확인할 수 있다.
>>```python
>> np.array([1, 2, 3, 4]).size  # 4
>>
>> np.array([[1, 2], [3, 4], [5, 6]]).size  # 6
>>```
>>
>>
>>
>> ## 5. Numpy 배열의 인덱싱과 슬라이싱
>> ### 5.1 Numpy 배열의 인덱싱
>> Numpy 배열은 아래와 같이 인덱싱(Indexing)할 수 있다.
>>```python
>> arr = np.arange(7)  # array([0, 1, 2, 3, 4, 5, 6])
>>
>> arr[3]
>> # 3
>> 
>> arr[7]
>> # IndexError: index 7 is out of bounds for axis 0 with size 7
>>
>> arr[0] = 10
>> # array([10, 1, 2, 3, 4, 5, 6])
>>```
>>
>>
>> ### 5.2 Numpy 배열의 슬라이싱
>> Numpy 배열은 아래와 같이 슬라이싱(Slicing)할 수 있다.
>>```python
>> arr = np.arange(7)  # array([0, 1, 2, 3, 4, 5, 6])
>>
>> arr[1:4]
>> # array([1, 2, 3])
>> 
>> arr[1:]
>> # array([1, 2, 3, 4, 5, 6])
>>
>> arr[:4]
>> # array([0, 1, 2, 3])
>>
>> arr[::2]
>> # array([0, 2, 4, 6])
>>```
>>
>>
>>
>> ## 6. Numpy 배열의 모양 바꾸기 및 배열 합치기, 나누기
>> ### 6.1 Numpy 배열의 모양 바꾸기 [reshape]
>> Numpy 배열은 **reshape**를 통해 모양을 바꿀 수 있다.
>>```python
>> arr1 = np.arange(8)  # array([0, 1, 2, 3, 4, 5, 6, 7])
>> arr1.shape  # (8,)
>>
>> arr2 = arr1.reshape((2, 4))
>> # array([[0, 1, 2, 3],
>> #       [4, 5, 6, 7]])
>> arr2.shape  # (2, 4)
>>```
>>
>>
>> ### 6.2 Numpy 배열 합치기 [concatenate]
>> Numpy 배열은 **concatenate**를 통해 합칠 수 있다.
>> ```python
>> arr1 = np.array([0, 1, 2])  # array([0, 1, 2])
>> arr2 = np.array([3, 4, 5])  # array([3, 4, 5])
>>
>> np.concatenate([arr1, arr2])
>> # array([0, 1, 2, 3, 4, 5])
>> ```
>>> #### 6.2.1 axis 속성 사용
>>> axis 속성에는 0, 1, None 값을 설정할 수 있다.
>>>
>>> axis 속성의 **Default 값은 0** 이다.
>>> ```python
>>> arr1 = np.array([[1, 2], [3, 4]])
>>> arr2 = np.array([[5, 6]])
>>>
>>> np.concatenate((arr1, arr2), axis=0)
>>> # array([[1, 2],
>>> #        [3, 4],
>>> #        [5, 6]])
>>>
>>> np.concatenate((arr1, arr2.T), axis=1)
>>> # array([[1, 2, 5],
>>> #        [3, 4, 6]])
>>>
>>> np.concatenate((arr1, arr2), axis=None)
>>> # array([1, 2, 3, 4, 5, 6])
>>> ```
>>
>>
>> ### 6.3 Numpy 배열 나누기 [split]
>> Numpy 배열은 **split**을 통해 나눌 수 있다.
>>
>> split 또한 axis 속성을 사용할 수 있다.
>>
>> axis 속성의 **Default 값은 0**이다.
>> ```python
>> matrix = np.arange(16).reshape(4, 4)
>> # array([[ 0,  1,  2,  3],
>> #        [ 4,  5,  6,  7],
>> #        [ 8,  9, 10, 11],
>> #        [12, 13, 14, 15]])
>>
>> # axis 속성이 0인 경우
>> upper, lower = np.split(matrix, [3], axis=0)
>>
>> upper
>> # array([[ 0,  1,  2,  3],
>> #        [ 4,  5,  6,  7],
>> #        [ 8,  9, 10, 11]])
>>
>> lower
>> # array([[12, 13, 14, 15]])
>>
>> # axis 속성이 1인 경우
>> left, right = np.split(matrix, [3], axis=0)
>>
>> left
>> # array([[ 0,  1,  2],
>> #        [ 4,  5,  6],
>> #        [ 8,  9, 10],
>> #        [12, 13, 14]])
>>
>> right
>> # array([[ 3],
>> #        [ 7],
>> #        [11],
>> #        [15]])
>> ```
>>
>>
>>
>> ## 7. Numpy 배열의 연산
>> ### 7.1 Numpy 배열의 기본 연산 방법 [Universal Function]
>> Numpy 배열은 기본적으로 +, -, *, /, % 등의 연산을 지원한다.
>> ```python
>> arr = np.arange(4)
>> # array([0, 1, 2, 3])
>> arr + 5
>> # array([5, 6, 7, 8])
>> arr - 5
>> # array([-5, -4, -3, -2])
>> arr * 5
>> # array([ 0,  5, 10, 15])
>> arr / 5
>> # array([0. , 0.2, 0.4, 0.6])
>> ```
>> 
>> 
>> ### 7.2 Numpy 배열의 다차원 행렬의 연산
>> Numpy 배열은 다차원 행렬의 연산도 지원한다.
>> ```python
>> arr1 = np.arange(4).reshape(2, 2)
>> # array([0, 1],
>> #       [2, 3])
>> arr2 = np.arange(4,8).reshape(2, 2)
>> # array([4, 5],
>> #       [6, 7])
>> arr1 + arr2
>> # array([[ 4,  6],
>> #        [ 8, 10]])
>> arr1 - arr2
>> # array([[-4, -4],
>> #        [-4, -4]])
>> ```
>> 
>> 
>> ### 7.3 Numpy 배열의 브로드캐스팅
>> Shape가 다른 배열끼리 연산 방법은 아래와 같다.
>> ```python
>> # [[6, 3, 4],                     [[7, 5, 7],
>> #  [1, 6, 4],   +  [1, 2, 3]  =    [2, 8, 7],
>> #  [4, 5, 2]])                     [5, 7, 5]])
>>
>> matrix = np.random.randint(1, 9, (3, 3))
>> # array([[6, 3, 4],
>> #        [1, 6, 4],
>> #        [4, 5, 2]])
>>
>> matrix + np.arange(1,4)  # matrix + array([1, 2, 3])
>> # array([[7, 5, 7],
>> #        [2, 8, 7],
>> #        [5, 7, 5]])
>>
>>
>> # [[0],                    [[0, 1, 2],
>> #  [1],   +  [0, 1, 2]  =   [1, 2, 3],
>> #  [2]]                     [2, 3, 4]]
>> 
>> arr1 = np.arange(3).reshape(3,1)
>> # array([[0],
>> #        [1],
>> #        [2]])
>> arr2 = np.arange(3)
>> # array([0, 1, 2])
>>
>> matrix = arr1 + arr2
>> # array([[0, 1, 2],
>> #        [1, 2, 3],
>> #        [2, 3, 4]])
>> ```
>>
>>
>>
>> ## 8. Numpy 배열의 집계함수 및 마스킹 연산
>> ### 8.1 Numpy 배열의 집계함수 [sum, min, max, mean, std]
>> 
>> ```python
>> arr = np.arange(8).reshape(2,4)
>> # array([[0, 1, 2, 3],
>> #        [4, 5, 6, 7]])
>> 
>> np.sum(arr)  # 28                ==  arr.sum()
>> np.min(arr)  # 0                 ==  arr.min()
>> np.max(arr)  # 7                 ==  arr.max()
>> np.mean(arr)  # 3.5              ==  arr.mean()
>> np.std(arr)  # 2.29128784747792  ==  arr.std()
>> 
>> np.sum(arr, axis=0)
>> # array([ 4,  6,  8, 10])
>> np.sum(arr, axis=1)
>> # array([ 6, 22])
>> ```
>> 
>>
>> ### 8.2 Numpy 배열의 마스킹 연산
>> ```python
>> arr = np.arange(5)  # array([0, 1, 2, 3, 4])
>> arr < 3  # array([ True,  True,  True, False, False])
>> arr > 5  # array([False, False, False, False, False])
>> arr[arr < 3]  # array([0, 1, 2])
>> ```
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
>> 
