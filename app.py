import numpy as np
import streamlit as st
import yfinance as yf

from hurst import hurst, classify, diffusion_regime

ticker = st.text_input("Ticker", "AAPL").upper()
years = st.slider("Lookback Period", 1, 10, 3)

if ticker:
    try