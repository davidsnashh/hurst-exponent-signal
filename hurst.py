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

    rng = np.random.default_rng(0)
    steps = np.diff(series)
    block = 20
    n_blocks = max(1, len(steps) // block)
    boot = []
    for _ in range(200):
        idx = rng.integers(0, n_blocks, n_blocks)
        sample = np.concatenate([steps[i * block:(i +1) * block] for i in idx])
        boot.append(slope_h(lags, msd(np.cumsum(sample), lags)))
    return {"H": H, "se": float(np.std(boot)), "lags": lags, "msd_curve": msd_curve}

def gbm_verdict(H, se):
    if H + 2 * se < 0.5:
        return "mean-reverting (gbm breaks)"
    if H -2 * se > 0.5:
        return "trending (gbm breaks)"
    return "no memory (gbm holds)"

def tail_stats(returns):
    r = np.asarray(returns, dtype=float).flatten()
    z = (r - r.mean()) / r.std()
    excess_kurtosis = float(np.mean(z ** 4) - 3.0)
    worst = float(z.min())
    p = 0.5 * (1 + math.erf(worst / math.sqrt(2)))
    gbm_years = float("inf") if p<= 0 else 1.0 / (p * 252)
    return {"excess_kurtosis": excess_kurtosis,"worst_sigma": worst, "gbm_years": gbm_years}

def vol_clustering(returns, lag=1):
    size = np.abs(returns)
    return float(np.corrcoef(size[lag:], size[:-lag])[0,1])