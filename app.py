import numpy as np
import streamlit as st
import yfinance as yf

from hurst import hurst, classify, diffusion_regime

ticker = st.text_input("Ticker", "AAPL").upper()
years = st.slider("Lookback Period", 1, 10, 3)

if ticker:
    try:
        data =yf.download(ticker, period=f"{years}y", auto_convert=True)
        close = data["Close"]

        logp = np.log(close)
        H, R2 = hurst(logp)

        c1, c2, c3 = st.columns(3)
        c1.metric("Hurst H", round(H, 3))
        c2.metric("Regime R2", classify(H))
        c3.metric("Scaling fit R", round(R2, 3))

st.write(f"{ticker.upper()} is {diffusion_regime(h)} over the last {years} years. (H = {H:.3f}).")
if r2 < 0.9:
    st.caption("A single power law fits the price series poorly here, read hurst H with a grain of salt")
    st.line_chart(close)

    except Exception:
    st.error("Could not load the ticker. Try another symbol.")