import streamlit as st
import pandas as pd
import plotly.express as px

from app.utils import carregar_dados

st.set_page_config(
    page_title="Dashboard Financeiro",
    layout="wide"
)

st.title("📊 Dashboard Atualizado por CSV")

# Sidebar
st.sidebar.title("Configurações")
if st.sidebar.button("🔄 Atualizar dados"):
    st.cache_data.clear()

# Dados
df = carregar_dados()

st.subheader("Tabela de Dados")
st.dataframe(df)

# Gráfico por categoria
st.subheader("Valores por Categoria")
grafico = df.groupby("categoria")["valor"].sum().reset_index()
st.bar_chart(grafico, x="categoria", y="valor")

# =========================
# GRÁFICO MENSAL
# =========================
df["data"] = pd.to_datetime(df["data"])

df_mensal = (
    df
    .groupby(pd.Grouper(key="data", freq="M"))["valor"]
    .sum()
    .reset_index()
)

df_mensal.columns = ["mes", "valor_total"]

fig = px.line(
    df_mensal,
    x="mes",
    y="valor_total",
    markers=True,
    title="Evolução Mensal dos Gastos - 2025"
)

st.plotly_chart(fig, use_container_width=True)
