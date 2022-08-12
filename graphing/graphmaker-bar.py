#!/usr/bin/env pythyon3

import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def main():
    fig = plt.figure(tight_layout=True)
    gs = gridspec.GridSpec(2, 2)

    ax = fig.add_subplot(gs[0, :])
    ax.plot(np.arange(0, 1e6, 1000))
    ax.set_ylabel('Caffeine Consumption, in liters')
    ax.set_xlabel('Coding Energy')

    for i in range(2):
        ax = fig.add_subplot(gs[1, i])
        ax.plot(np.arange(1., 0., -0.1) * 2000., np.arange(1., 0., -0.1))
        ax.set_ylabel('More Coffee %d' % i)
        ax.set_xlabel('Meme Browsing %d' % i)
        if i == 0:
            for tick in ax.get_xticklabels():
                tick.set_rotation(55)
    fig.align_labels()  # same as fig.align_xlabels(); fig.align_ylabels()






    plt.title("How I Get Work Done")
    plt.savefig("/home/student/static/Coffee.png")

if __name__ == "__main__":
    main()
