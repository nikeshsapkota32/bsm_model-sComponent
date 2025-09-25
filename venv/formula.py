import streamlit as st
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# --- Black-Scholes-Merton Model Function (from previous step) ---
def black_scholes_merton(S, K, T, r, sigma):
    """
    Calculates the price of a European call and put option using the
    Black-Scholes-Merton model.
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    put_price = K * np.exp(-r * T) * norm.cdf(-d1) - S * norm.cdf(-d1) # Corrected N(-d1) for put

    return call_price, put_price

# --- Streamlit Web Application ---
st.set_page_config(layout="wide") # Use wide layout for better space utilization
st.title("Black-Scholes-Merton Option Pricing Model")

st.write("""
This application calculates the theoretical price of European call and put options
using the Black-Scholes-Merton model.
""")

# Input Sidebar
st.sidebar.header("Input Parameters")

# Sliders and Number Inputs for BSM parameters
S = st.sidebar.slider("Current Stock Price (S)", 50.0, 500.0, 100.0, 5.0)
K = st.sidebar.slider("Strike Price (K)", 50.0, 500.0, 100.0, 5.0)
T = st.sidebar.slider("Time to Expiration (T, in years)", 0.1, 5.0, 1.0, 0.1)
r = st.sidebar.slider("Risk-Free Interest Rate (r)", 0.01, 0.10, 0.05, 0.005)
sigma = st.sidebar.slider("Volatility (sigma)", 0.05, 0.80, 0.20, 0.01)

# Calculate prices
call_price, put_price = black_scholes_merton(S, K, T, r, sigma)

# Display Results
st.subheader("Calculated Option Prices")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="European Call Option Price", value=f"${call_price:.2f}")
with col2:
    st.metric(label="European Put Option Price", value=f"${put_price:.2f}")

st.markdown("---") # Separator

### Step 4: Adding Basic Visualization

# Let's add a plot to show how the option price changes with the underlying stock price.

#### Visualize Option Price vs. Stock Price
st.subheader("Option Price vs. Stock Price")

# Create a range of stock prices for plotting
stock_prices = np.linspace(S * 0.7, S * 1.3, 100) # From 70% to 130% of current S
call_prices_plot = []
put_prices_plot = []

for stock_price in stock_prices:
    c, p = black_scholes_merton(stock_price, K, T, r, sigma)
    call_prices_plot.append(c)
    put_prices_plot.append(p)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(stock_prices, call_prices_plot, label="Call Option Price", color='blue')
ax.plot(stock_prices, put_prices_plot, label="Put Option Price", color='red')
ax.axvline(K, color='gray', linestyle='--', label='Strike Price')
ax.set_xlabel("Stock Price (S)")
ax.set_ylabel("Option Price")
ax.set_title("Option Price Sensitivity to Stock Price")
ax.legend()
ax.grid(True)
st.pyplot(fig) # Display the plot in Streamlit