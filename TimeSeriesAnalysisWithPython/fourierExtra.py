# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 17:17
# @Author  : sen
import numpy as np
import pylab as pl
from scipy import signal
from numpy import fft

def fourierExtrapolation(x, n_predict):
    n = len(x)
    n_harm = 50                        # number of harmonics in model
    t = np.arange(0, n)
    p = np.polyfit(t, x, 1)            # find linear trend in x
    x_notrend = x - p[0] * t        # detrended x
    x_freqdom = fft.fft(x_notrend)    # detrended x in frequency domain
    f = fft.fftfreq(n)                # frequencies
    indexes = list(range(n))
    # sort indexes by frequency, lower -> higher
    indexes.sort(key = lambda i: np.absolute(f[i]))
    t = np.arange(0, n + n_predict)
    restored_sig = np.zeros(t.size)
    for i in indexes[:1 + n_harm * 2]:
        ampli = np.absolute(x_freqdom[i]) / n    # amplitude
        phase = np.angle(x_freqdom[i])             # phase
        restored_sig += ampli * np.cos(2 * np.pi * f[i] * t + phase)
    return ((restored_sig + p[0] * t),x_freqdom/100)

def main():
    t = np.linspace(0, 1, 500)
    #y = list(signal.sawtooth((2 * np.pi * 5 * t ),0.5))
    y = list(np.sin(2 * np.pi * 5 * t))
    n_predict = 1000
    extrapolation, frequency = fourierExtrapolation(y, n_predict)
    pl.plot(np.arange(0, 500), y, 'r', label = 'triangle')
    pl.plot(np.arange(0, 500), frequency, 'g', label = 'frequency')
    pl.plot(np.arange(0, extrapolation.size), extrapolation, 'b', label = 'extrapolation')
    pl.legend()
    pl.show()

if __name__ == "__main__":
    main()
