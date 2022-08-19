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
<image src="https://user-images.githubusercontent.com/110414297/185342023-2e1961d3-317a-43f2-90ac-e012ca4c80aa.png"/>

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
<image src="https://user-images.githubusercontent.com/110414297/185382313-6d21dd4e-93a0-45e7-af5b-481ff42de926.png"/>

## 3. 그래프의 종류 및 속성
### 3.1 Line Graph
#### 3.1.1 Linestyle
```python
x = np.arange(10)
fig, ax = plt.subplots()

ax.plot(x, x, linestyle="-")    # solid
ax.plot(x, x+2, linestyle="--") # dashed
ax.plot(x, x+4, linestyle="-.") # dashdot
ax.plot(x, x+6, linestyle=":")  # dotted
```
<image src="https://user-images.githubusercontent.com/110414297/185592278-d5e67f0a-f42f-4649-90f9-dea00e22df4d.png"/>


#### 3.1.2 Color
```python
ax.plot(x, x, color="r")    # r, g, b, c, m, y, k, w
ax.plot(x, x+2, color="green") # red, green, blue, cyan...
ax.plot(x, x+4, color="0.8") # 0 ~ 1
ax.plot(x, x+6, color="#524FA1")  # color code(hex)
```
<image src="https://user-images.githubusercontent.com/110414297/185592384-6320535a-e3c8-498d-a0ce-9b37ac727ca4.png"/>


#### 3.1.3 Marker
```python
ax.plot(x, x, marker=".")
ax.plot(x, x+2, marker="o")
ax.plot(x, x+4, marker="v")
ax.plot(x, x+6, marker="s")
ax.plot(x, x+8, marker="*")
```
<image src="https://user-images.githubusercontent.com/110414297/185592444-ab918ec5-a207-4c6e-b6e6-997352c05f02.png"/>



#### 3.1.4 범례 설정
```python
fig, ax = plt.subplots()
ax.plot(x, x, label='y=x')
ax.plot(x, x**2, label='y=x^2')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend(
    loc='upper right', # lower/center/upper  left/center/right
    shadow=True,
    fancybox=True, # 모서리 둥글게
    borderpad=2 # Padding 값 조정
)
```
<image src="https://user-images.githubusercontent.com/110414297/185571800-5ed6e8d0-ad29-4782-9075-55213a327210.png"/>


#### 3.1.5 축 경계 조정하기
```python
x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x))
ax.set_xlim(-2, 12)
ax.set_ylim(-1.5, 1.5)
```
<image src="https://user-images.githubusercontent.com/110414297/185567208-680f0a58-a780-482f-8a79-52c48f1cb47b.png"/>


### 3.2 Scatter Graph
```python
fig, ax = plt.subplots()
x = np.arange(10)

ax.plot(
    x, x**2, "o",
    markersize=15,
    markerfacecolor='white',
    markeredgecolor='red'
)
```
<image src="https://user-images.githubusercontent.com/110414297/185573789-fcca8d42-448e-42b7-a415-287a63af5ce6.png"/>

```python
fig, ax = plt.subplots()
x = np.random.randn(50)
y = np.random.randn(50)
colors = np.random.randint(0, 100, 50)
sizes = 500 * np.pi * np.random.rand(50) ** 2

ax.scatter(
    x, y,
    c=colors,   # 색상
    s=sizes,    # 사이즈
    alpha=0.2   # 투명도
)
```
<image src="https://user-images.githubusercontent.com/110414297/185574951-f68f15fa-ebbb-4e7c-b66d-bbe5618d9d6e.png"/>


### 3.3 Bar Graph
```python
x = np.arange(10)
# figsize 속성으로 그래프의 가로, 세로 길이를 조절 가능하다
fig, ax = plt.subplots(figsize=(12, 4))
ax.bar(x, x*2)
```
<image src="https://user-images.githubusercontent.com/110414297/185591922-f16d5d60-7563-45b1-9394-df37b065a703.png"/>


#### 3.3.1 누적 Bar Graph
```python
x = np.random.rand(3)
y = np.random.rand(3)
z = np.random.rand(3)
data = [x, y, z]

fig, ax = plt.subplots()
x_ax = np.arange(3)

for i in x_ax:
    ax.bar(x_ax, data[i],
           bottom=np.sum(data[:i], axis=0))
ax.set_xticks(x_ax)
ax.set_xticklabels(["A", "B", "C"])
```
<image src="https://user-images.githubusercontent.com/110414297/185603153-7091150b-bf32-4616-aa74-83e26ef80485.png"/>


#### 3.4 Histogram Graph
```python
fig, ax = plt.subplots()
data = np.random.randn(1000)
# bins속성을 이용해 하나의 막대에 몇개의 데이터를 넣을지 설정 가능
ax.hist(data, bins=50)
```
<image src="https://user-images.githubusercontent.com/110414297/185604467-980cc4e0-43d0-4334-b12c-d5439b1ff355.png"/>


## 4. 
