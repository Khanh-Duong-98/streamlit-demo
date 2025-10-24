import streamlit as st
import pandas as pd
import numpy as np

# ---- App title ----
st.title("🚀 Streamlit Demo App")

# ---- Sidebar ----
st.sidebar.header("Options")
num_points = st.sidebar.slider("Number of data points", 10, 200, 50)
show_table = st.sidebar.checkbox("Show raw data")

# ---- Generate random data ----
data = pd.DataFrame(
    np.random.randn(num_points, 2),
    columns=["X", "Y"]
)

# ---- Display ----
st.subheader("Random Data Chart")
st.line_chart(data)

if show_table:
    st.subheader("Raw Data")
    st.dataframe(data)

# ---- Simple input ----
st.subheader("User Input")
name = st.text_input("What's your name?")
if name:
    st.success(f"Hello, {name}! 👋")

# ---- Footer ----
st.caption("Built with ❤️ using Streamlit")