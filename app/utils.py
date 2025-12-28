import pandas as pd
import streamlit as st

@st.cache_data(ttl=60)
def carregar_dados():
    return pd.read_csv("data/dados.csv")
