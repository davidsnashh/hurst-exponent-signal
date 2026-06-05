import numpy as np
import streamlit as st
import yfinance as yf
import math

from hurst import diffusion, gbm_verdict, tail_stats, vol_clustering

st.title("GBM Stress Test")


ticker = st.text_input("Ticker", "AAPL").upper()
years = st.slider("Lookback Period", 1, 10, 3)

