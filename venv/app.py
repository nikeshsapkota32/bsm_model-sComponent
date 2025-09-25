import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Import the functions from our new file
from formula import black_scholes_merton, calculate_greeks

# --- Streamlit Web Application ---
st.set_page_config(layout="wide")
st.title("Black-Scholes-Merton Option Pricing & Greeks Calculator")

st.write("""
This application calculates the theoretical price of European call and put options
and their risk sensitivities (Greeks).
""")

# Input Sidebar
st.sidebar.header("Input Parameters")
S = st.sidebar.slider("Current Stock Price (S)", 50.0, 500.0, 100.0, 5.0)
K = st.sidebar.slider("Strike Price (K)", 50.0, 500.0, 100.0, 5.0)
T = st.sidebar.slider("Time to Expiration (T, in years)", 0.1, 5.0, 1.0, 0.1)
r = st.sidebar.slider("Risk-Free Interest Rate (r)", 0.01, 0.10, 0.05, 0.005)
sigma = st.sidebar.slider("Volatility (sigma)", 0.05, 0.80, 0.20, 0.01)

# Main Content Area
col1, col2 = st.columns(2)

with col1:
    st.header("Option Prices")
    call, put = black_scholes_merton(S, K, T, r, sigma)
    st.metric(label="European Call Price", value=f"${call:.2f}")
    st.metric(label="European Put Price", value=f"${put:.2f}")

with col2:
    st.header("The Greeks")
    greeks = calculate_greeks(S, K, T, r, sigma)
    st.metric(label="Delta (Call)", value=f"{greeks['delta_call']:.3f}")
    st.metric(label="Delta (Put)", value=f"{greeks['delta_put']:.3f}")
    st.metric(label="Gamma", value=f"{greeks['gamma']:.3f}")
    st.metric(label="Theta (Call)", value=f"{greeks['theta_call']:.3f}")
    st.metric(label="Vega", value=f"{greeks['vega']:.3f}")
    st.metric(label="Rho (Call)", value=f"{greeks['rho_call']:.3f}")

st.markdown("---")

# Visualization
st.header("Option Price vs. Stock Price")
stock_prices = np.linspace(S * 0.7, S * 1.3, 100)
call_prices_plot = [black_scholes_merton(sp, K, T, r, sigma)[0] for sp in stock_prices]
put_prices_plot = [black_scholes_merton(sp, K, T, r, sigma)[1] for sp in stock_prices]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(stock_prices, call_prices_plot, label="Call Option Price", color='blue')
ax.plot(stock_prices, put_prices_plot, label="Put Option Price", color='red')
ax.axvline(K, color='gray', linestyle='--', label='Strike Price')
ax.set_xlabel("Stock Price (S)")
ax.set_ylabel("Option Price")
ax.legend()
ax.grid(True)
st.pyplot(fig)