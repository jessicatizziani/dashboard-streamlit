import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
from app.utils import carregar_dados

st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

st.title("📊 Dashboard Atualizado por CSV")

st.sidebar.title("Configurações")
if st.sidebar.button("🔄 Atualizar dados"):
    st.cache_data.clear()

df = carregar_dados()

st.subheader("Tabela de Dados")
st.dataframe(df)

# Gráfico por categoria
st.subheader("Valores por Categoria")
grafico = df.groupby("categoria")["valor"].sum().reset_index()

st.bar_chart(grafico, x="categoria", y="valor")


# Gráfico mensal
fig = px.line(
    df_mensal,
    x="mes",
    y="valor_total",
    markers=True,
    title="Evolução Mensal dos Gastos - 2025"
)

fig.update_layout(
    xaxis_title="Mês",
    yaxis_title="Valor Total (R$)",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)


@st.cache_data(ttl=60)
def carregar_dados():
    return pd.read_csv("data/seu_arquivo.csv")