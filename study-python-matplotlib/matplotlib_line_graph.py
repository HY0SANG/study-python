import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(10)
fig, ax = plt.subplots()
ax.plot(
    x, x, label='y=x',
    marker='o',
    color='blue',
    linestyle=':'
)
ax.plot(
    x, x**2, label='y=x^2',
    marker='^',
    color='red',
    linestyle='--'
)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend(
    loc='upper left',
    shadow=True,
    fancybox=True,
    borderpad=2
)

fig.savefig("plot.png")
