import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Stock Analytics Dashboard", page_icon="📈", layout="wide")

st.title("📊 Smart Stock Analytics Dashboard")
st.write("Interactive stock market analysis using real-time financial data.")

# Sidebar controls
st.sidebar.header("Dashboard Controls")

stock = st.sidebar.selectbox(
    "Choose a Company",
    ("INFY.NS","TCS.NS","RELIANCE.NS","HDFCBANK.NS","WIPRO.NS")
)

start = st.sidebar.date_input("Start Date", pd.to_datetime("2020-01-01"))
end = st.sidebar.date_input("End Date", pd.to_datetime("2025-01-01"))

# Download data
data = yf.download(stock, start=start, end=end)

st.subheader(f"Stock Data for {stock}")
st.dataframe(data.tail())

# Key metrics
col1, col2, col3 = st.columns(3)

col1.metric("Latest Close Price", round(data['Close'].iloc[-1],2))
col2.metric("Highest Price", round(data['High'].max(),2))
col3.metric("Lowest Price", round(data['Low'].min(),2))

# Closing price chart
st.subheader("📈 Closing Price Trend")

fig, ax = plt.subplots()
ax.plot(data.index, data['Close'])
ax.set_xlabel("Date")
ax.set_ylabel("Price")
st.pyplot(fig)

# Volume chart
st.subheader("📊 Trading Volume")

fig2, ax2 = plt.subplots()
ax2.plot(data.index, data['Volume'])
ax2.set_xlabel("Date")
ax2.set_ylabel("Volume")
st.pyplot(fig2)

# Moving averages
data['MA50'] = data['Close'].rolling(50).mean()
data['MA200'] = data['Close'].rolling(200).mean()

st.subheader("📉 Moving Average Analysis")

fig3, ax3 = plt.subplots()
ax3.plot(data.index, data['Close'], label="Close Price")
ax3.plot(data.index, data['MA50'], label="50 Day Average")
ax3.plot(data.index, data['MA200'], label="200 Day Average")
ax3.legend()
st.pyplot(fig3)

st.success("Dashboard loaded successfully 🚀")