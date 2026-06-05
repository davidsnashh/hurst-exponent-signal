import numpy as np
import math

def msd(series, lags):
    return np.array([np.var(series[lag:] - series[:-lag]) for lag in lags])

def slope_h(lags, msd_values):
    return np.polyfit(np.log(lags), np.log(msd_values), deg=1)[0] / 2.0

def diffusion(series, lags=range(2, 20)):
    series = np.asarray(series, dtype=float).flatten()
    lags = np.array(list(lags))
    msd_curve = msd(series, lags)
    H = slope_h(lags, msd_curve)

    random = np.random.random()
    steps = np.diff(series)
    block = 20
    n_blocks = max(1, len(steps) // block)
    boot = []
    for _ in range(200):
        idx = rng.integers(0, n_blocks, n_blocks)