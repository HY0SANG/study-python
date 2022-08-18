# Matplotlib

## 1. Matplotlib의 개요
### 1.1 Matplotlib이란?
파이썬에서 데이터를 그래프나 차트로 시각화할 수 있는 라이브러리이다.

### 1.2 Matplotlib import 방법
Matplotlib는 관습적으로 **plt**로 줄여씀
```python
import matplotlib.pyplot as plt
```

## 2. 그래프 그리기
```python
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

plt.plot(x, y)
plt.title("First Plot")
plt.xlabel("x")
plt.ylabel("y")
```
<image src="https://user-images.githubusercontent.com/110414297/185342023-2e1961d3-317a-43f2-90ac-e012ca4c80aa.png" width="350px">

