import sys
from scramblefromfile import (
    times,
    times_3x3,
    times_4x4,
    times_5x5,
    times_6x6,
    times_7x7,
    all_times
)
import matplotlib.pyplot as plt
from math import ceil
import numpy as np


def plot_times(times):
    m = min(times)
    n = max(times)

    x = np.linspace(1, len(times), len(times))
    z = np.polyfit(x, times, 1)
    p = np.poly1d(z)
    plt.step(x, times, color="c")
    plt.grid(axis="y", linestyle="-", linewidth=1)
    plt.plot(x, p(x), "--", color="k")
    plt.show()

    xp = np.linspace(ceil(m) - 1, ceil(n), round(ceil(n) - ceil(m) + 2))
    # print(ceil(m)-1,ceil(n),round(ceil(n)-ceil(m)+2))
    plt.hist(times, xp, alpha=1, width=0.8)
    plt.xlim(m - 1, n + 1)
    plt.grid(axis="y", linestyle="-", linewidth=1)
    plt.show()


if __name__ == "__main__":

    if len(sys.argv) == 3:
        cube = all_times[(int(sys.argv[2])-3)]
        plot_times(cube)

    else:
        plot_times(times)
