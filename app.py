import numpy as np
import streamlit as st
import yfinance as yf

from hurst import diffusion, gbm_verdict, tail_stats, vol_clustering

st.title("GBM Stress Test")
st.write("GBM estimates: H = 0.5, Excess Kurtosis = 0, Clustering = 0")

ticker = st.text_input("Ticker", "AAPL").upper()
years = st.slider("Lookback Period", 1, 10, 3)

if ticker:
    try:
        close = yf.download(ticker, period=f"years}y", auto_adjust=True)["Close"].dropna()
        logp = np.log(close.values).flatten()
        returns = np.diff(logp)

        c1, c2, c3 = st.columns(3)
        c1.metric("Hurst H", round(H, 3))
        c2.metric("Regime", classify(H))
        c3.metric("Scaling fit R2", round(R2, 3))

        st.write(f"{ticker.upper()} is {diffusion_regime(H)} over the last {years} years. (H = {H:.3f}).")
        if R2 < 0.9:
            st.caption("A single power law fits the price series poorly here, read hurst H with a grain of salt")
        st.line_chart(close)

    except Exception:
        st.error("Could not load the ticker. Try another symbol.")