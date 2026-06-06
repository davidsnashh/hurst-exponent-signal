# Anomalous Diffusion Test of Geometric Brownian Motion
This tool treats a stock's log-price like a diffusing particle and tests it under GBM assumptions, type the ticker and see where the model breaks.
### Live Demo:
#### https://davidsnashh-hurst-exponent-signal-app-e7y55b.streamlit.app
## Background
**The Hurst Exponent.** Describes how a wandering quantity spreads out over time, as the time window size changes how much more displacement do we see? The exponent captures the reinforcing properties (or lack thereof) of the steps involved in a process. Nearing 0 the steps tend to "fight eachother", nearing 0.5 they display independence, nearing 1.0 the steps reinforce and continue.

**Anomalous Diffusion.** Diffusion describes the spread of something through an environment such that the distance from the start grows proportionately to the square root of elapsed time, indicating each step is independent of the last. Anomalous Diffusion is any spread that breaks the base assumptions. Superdiffusion is when steps persist and the spread grows faster, subdiffusion is when steps cancel eachother growing the spread slower.

**Geometric Brownian Motion.** commonly models how price modes through time. It suggests that over any time interval the price changes by a random percentage and in the next interval it does the same, fully independent of the last and arw drawn from a distribution with constant width.

# The three tests
## Memory.
GBM assumes moves carry no memory. The tool measures the Hurst exponent: near one half is a memoryless walk, below is mean reversion, above is momentum. Liquid stocks read near one half, the correct result, since reliable direction would be a free signal traders compete away; real departures live mostly in spreads, some crypto, or longer horizons.
## Tails.
GBM assumes moves follow a bell curve, making large moves vanishingly rare. The tool measures excess kurtosis and reports the worst day in standard deviations with how often a bell curve allows it. Real markets are heavy-tailed (Mandelbrot saw this in 1960s cotton prices), so a crash the model calls once-in-millennia shows up every few years. This is what makes option prices and risk figures understate severe losses.
## Volatility.
GBM assumes move sizes stay constant. The tool measures whether one day's move size correlates with the previous day's. Real markets show a strong, slowly fading correlation: volatility comes in storms and lulls, not at a steady level. In physics this is a diffusion rate that changes over time; in finance it is volatility clustering.

## Limitations
Measured at the daily scale, where behavior can differ from longer horizons. The Hurst estimate is noisy on shorter windows (the error bar shows it), and an exponent is a simplification since markets are mildly multifractal. The tail figure is the worst downside day. Data comes from Yahoo Finance via yfinance, which can fight cloud hosts, and every result reflects the user chosen window rather than a fixed property.

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```
---

built by David Nash, math + physics @BU