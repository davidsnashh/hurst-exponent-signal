import numpy as np
import math

def hurst(series, lags=range(2, 20)):
    lags = np.array(list(lags))
    msd = np.array([np.var(series[lag:] - series[:-lag]) for lag in lags]) #msd = mean squared displacement, tracks how far a system wanders from the start over time

    log_lag, log_msd = np.log(lags), np.log(msd)
    slope, intercept = np.polyfit(log_lag, log_msd, 1) #fits a line by least squares
    h = slope / 2.0

    model = slope * log_lag + intercept
    r2 = 1.0 - np.sum((log_msd - model) ** 2) / np.sum((log_msd - log_msd.mean()) ** 2)
    return h, r2

def classify(h):
    if h < 0.45:
        return "mean-reverting"
    elif h > 0.55:
        return "trending"
    return "random walk"

def diffusion_regime(h):
    if h < 0.45:
        return "subdiffusive"
    elif h > 0.55:
        return "superdiffusive"
    return "normal (Brownian)"