import numpy as np
import streamlit as st
import yfinance as yf

from hurst import diffusion, gbm_verdict, tail_stats, vol_clustering

st.title("GBM Estimate versus Hurst Exponent Test")
st.write("GBM assumptions would suggest: H = 0.5, Excess Kurtosis = 0, Clustering = 0")

ticker = st.text_input("Ticker", "AAPL").upper()
years = st.slider("Lookback Period", 1, 10, 3)

if ticker:
    try:
        close = yf.download(ticker, period=f"{years}y", auto_adjust=True)["Close"].dropna()
        logp = np.log(close.values).flatten()
        returns = np.diff(logp)

        d = diffusion(logp)
        H, se = d['H'], d['se']
        tails = tail_stats(returns)
        vc = vol_clustering(returns)

        c1, c2, c3 = st.columns(3)
        c1.metric("Hurst H", f"{H:.2f} +/- {se:.2f}", help="Hurst is the memory in the daily moves, below 0.5 suggests reversion, above 0.5 suggests continuity, 0.5 suggests a gbm-esque walk")
        c2.metric("Excess kurtosis", f"{tails['excess_kurtosis']:.1f}", help="Excess Kurtosis measures how fat the return distribution's tails are, aka how often extreme days in any direction happen, the aforementioned walk suggests an ek near 0, the higher the ek the more common extreme events are")
        c3.metric("Vol Clustering", f"{vc:.2f}", help="Volatility clustering measures how often high vol days cluster around eachother, the walk assumes constant volatility so 0")

        st.write(f"**{ticker}**: where the metrics drift from the assumptions is where GBM breaks. Worst Day {tails['worst_sigma']:.1f} sigma. GBM says this would happen once every {tails['gbm_years']:,.0f} years.")
        st.line_chart(close)

    except Exception as e:
        st.error(e)