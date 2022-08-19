import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

# 그래프를 그리는 코드 작성
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("first_plot")
ax.set_xlabel("x")
ax.set_ylabel("y")


# 그래프를 first_plot.png 파일로 저장
fig.set_dpi(300)
fig.savefig("first_plot.png")
