import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 의 pyplot으로 그래프를 그릴 때, 기본 폰트는 한글을 지원하지 않음
# 한글 지원 폰트로 직접 바꾸어주면 한글을 사용할 수 있다.
import matplotlib.font_manager as fm
fname='./NanumBarunGothic.ttf'
font = fm.FontProperties(fname = fname).get_name()
plt.rcParams["font.family"] = font


x = np.array(["축구", "야구", "농구", "배드민턴", "탁구"])
y = np.array([18, 7, 12, 10, 8])

z = np.random.randn(1000)


fig, axes = plt.subplots(1, 2, figsize=(8, 4))

# Bar 그래프
axes[0].bar(x, y)
# 히스토그램
axes[1].hist(z, bins = 50)

fig.savefig("plot.png")
