import pandas as pd

def carregar_dados(caminho="data/dados.csv"):
    df = pd.read_csv(caminho)
    return df


