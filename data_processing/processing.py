# poetry run processing.py

# 📁 01_data_ingestion/load_data.py

import pandas as pd
from pathlib import Path

# Caminho fixo fornecido
CAMINHO_ARQUIVO = Path("C:/Users/Administrador/Downloads/campaigns.csv")

def carregar_dados(caminho=CAMINHO_ARQUIVO):
    try:
        df = pd.read_csv(caminho)
        print("✅ Dados carregados com sucesso!")
        print(f"🔎 Dataset: {df.shape[0]} linhas × {df.shape[1]} colunas")
        return df
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado em: {caminho}")
    except Exception as e:
        print(f"⚠️ Erro ao carregar o arquivo: {e}")

if __name__ == "__main__":
    df = carregar_dados()
    if df is not None:
        print("📋 Colunas do DataFrame:")
        print(df.columns.tolist())

        # Filtrar 'Audience'
        df_filtrado = df[df["Audience"].str.contains("ClearerThinking.org", case=False, na=False)]
        print(f"📊 Linhas após filtro: {df_filtrado.shape[0]}")

        # Converter 'Send Date' para datetime
        df_filtrado["Send Date"] = pd.to_datetime(df_filtrado["Send Date"], errors="coerce")

        # Criar colunas formatadas de data e hora (strings)
        df_filtrado["Data"] = df_filtrado["Send Date"].dt.strftime("%d/%m/%Y")
        df_filtrado["Hora"] = df_filtrado["Send Date"].dt.strftime("%H:%M:%S")

        # Remover as colunas indesejadas
        df_filtrado = df_filtrado.drop(columns=["Send Date"])

        print(df_filtrado[["Data", "Hora"]].head())

    else:
        print("⚠️ O DataFrame não foi carregado.")


