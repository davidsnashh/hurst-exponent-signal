# Anamalous Diffusion Test of Geometric Brownian Motion
This tool treats a stock's log-price like a diffusing particle and tests it under GBM assumptions, type the ticker and see where the model breaks.
### Live Demo:
#### https://davidsnashh-hurst-exponent-signal-app-e7y55b.streamlit.app
## Background
**The Hurst Exponent.** Describes how a wandering quantity spreads out over time, as the time window size changes how much more displacement do we see? The exponent captures the reinforcing properties (or lack thereof) of the steps involved in a process. Nearing 0 the steps tend to "fight eachother", nearing 0.5 they display independence, nearing 1.0 the steps cluster together.

**Anamalous Diffusion.**