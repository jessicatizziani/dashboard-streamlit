import streamlit as st
import pandas as pd
import plotly.express as px

from utils import carregar_dados

st.set_page_config(
    page_title="Dashboard Financeiro",
    layout="wide"
)

st.title("📊 Dashboard Financeiro")

# Sidebar
st.sidebar.header("Configurações")
if st.sidebar.button("🔄 Atualizar dados"):
    st.cache_data.clear()

# Dados
df = carregar_dados()

st.subheader("Tabela de Dados")
st.dataframe(df)

# Gráfico por categoria
st.subheader("Valores por Categoria")
grafico_categoria = (
    df.groupby("categoria", as_index=False)["valor"].sum()
)

st.bar_chart(grafico_categoria, x="categoria", y="valor")

# Gráfico mensal
df["data"] = pd.to_datetime(df["data"])
df["mes"] = df["data"].dt.to_period("M").astype(str)

df_mensal = (
    df.groupby("mes", as_index=False)["valor"].sum()
    .rename(columns={"valor": "valor_total"})
)

fig = px.line(
    df_mensal,
    x="mes",
    y="valor_total",
    markers=True,
    title="Evolução Mensal dos Gastos"
)

st.plotly_chart(fig, use_container_width=True)
