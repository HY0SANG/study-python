# Matplotlib

## 1. Matplotlib의 개요
### 1.1 Matplotlib이란?
파이썬에서 데이터를 그래프나 차트로 시각화할 수 있는 라이브러리이다.

### 1.2 Matplotlib import 방법
Matplotlib는 관습적으로 **plt**로 줄여씀
```python
import matplotlib.pyplot as plt
```
### 1.3 Matplotlib figure의 구조
<image src="https://user-images.githubusercontent.com/110414297/185372425-9935fddd-f6d3-4721-a06f-ad655ec2e30b.png" width="500px"/>



## 2. 그래프 그리고 저장하기
### 2.1 그래프 그리기
```python
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Frist Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")
```
<image src="https://user-images.githubusercontent.com/110414297/185342023-2e1961d3-317a-43f2-90ac-e012ca4c80aa.png" width="350px"/>

### 2.2 그래프 저장하기
```python
# 화질 조절 가능, dpi == doth per inch
fig.set_dpi(300)
# first_plot.png 파일로 저장하기
fig.savefig("first_plot.png")
```
  
### 2.3 여러개 그래프 그리기
```python
x = np.linspace(0, np.pi*4, 100)

fig, axes = plt.subplots(2, 1)
axes[0].plot(x, np.sin(x))
axes[1].plot(x, np.cos(x))
```
<image src="https://user-images.githubusercontent.com/110414297/185382313-6d21dd4e-93a0-45e7-af5b-481ff42de926.png" width="350px"/>

## 3. 그래프의 종류 및 속성
### 3.1 Line plot
#### 3.1.1 Linestyle
```python
x = np.arange(10)
fig, ax = plt.subplots()

ax.plot(x, x, linestyle="-")    # solid
ax.plot(x, x+2, linestyle="--") # dashed
ax.plot(x, x+4, linestyle="-.") # dashdot
ax.plot(x, x+6, linestyle=":")  # dotted
```
<image src="https://user-images.githubusercontent.com/110414297/185383866-a87101ac-d013-4547-a002-47f63b19db58.png" width="350px"/>

#### 3.1.2 Color
```python
ax.plot(x, x, color="r")    # r, g, b, c, m, y, k, w
ax.plot(x, x+2, color="green") # red, green, blue, cyan...
ax.plot(x, x+4, color="0.8") # 0 ~ 1
ax.plot(x, x+6, color="#524FA1")  # color code(hex)
```
<image src="https://user-images.githubusercontent.com/110414297/185386210-7cae8461-5f73-48ac-81d2-7f5cff63e2f6.png" width="350px"/>

#### 3.1.3 Marker
```python
ax.plot(x, x, marker=".")
ax.plot(x, x+2, marker="o")
ax.plot(x, x+4, marker="v")
ax.plot(x, x+6, marker="s")
ax.plot(x, x+8, marker="*")
```
<image src="https://user-images.githubusercontent.com/110414297/185386798-ab354007-bb51-4ee8-92b8-fbd2601d1fdd.png" width="350px"/>
