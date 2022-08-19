import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x = np.arange(10)
ax.plot(
    x, x**2, "o",
    markersize=15,
    markerfacecolor='white',
    markeredgecolor="blue"
)

fig.savefig("plot.png")
