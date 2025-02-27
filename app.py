import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Configuração inicial da página
st.set_page_config(page_title="Análise de Dados Agrícolas", layout="wide")

# Título da aplicação
st.title("📊 Análise de Dados Agrícolas com Streamlit")

# Upload do arquivo CSV
st.sidebar.header("Upload do Arquivo")
uploaded_file = st.sidebar.file_uploader("Escolha um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # Carregar o arquivo CSV
    df = pd.read_csv(uploaded_file)

    # Exibir os primeiros registros
    st.subheader("Visualização dos Dados")
    st.write("Primeiras 5 linhas do arquivo:")
    st.dataframe(df.head())

    # Informações gerais sobre o dataset
    st.subheader("Resumo do Dataset")
    st.write(f"Número de linhas: {df.shape[0]}")
    st.write(f"Número de colunas: {df.shape[1]}")
    st.write("Tipos de dados:")
    st.write(df.dtypes)

    # Filtros
    st.sidebar.header("Filtros")
    soil_types = df["Soil Type"].unique()
    crop_types = df["Crop Type"].unique()
    fertilizer_names = df["Fertilizer Name"].unique()

    selected_soil = st.sidebar.multiselect("Selecione o Tipo de Solo", soil_types, default=soil_types)
    selected_crop = st.sidebar.multiselect("Selecione o Tipo de Cultura", crop_types, default=crop_types)
    selected_fertilizer = st.sidebar.multiselect("Selecione o Nome do Fertilizante", fertilizer_names, default=fertilizer_names)

    # Filtrar o DataFrame
    filtered_df = df[
        (df["Soil Type"].isin(selected_soil)) &
        (df["Crop Type"].isin(selected_crop)) &
        (df["Fertilizer Name"].isin(selected_fertilizer))
    ]

    if filtered_df.empty:
        st.warning("Nenhum dado corresponde aos filtros selecionados.")
    else:
        st.subheader("Dados Filtrados")
        st.dataframe(filtered_df)

        # Gráficos
        st.subheader("Gráficos Interativos")

        # Gráfico 1: Distribuição de Temperatura e Umidade
        st.write("### Distribuição de Temperatura e Umidade")
        fig = px.scatter(filtered_df, x="Temperature", y="Humidity", color="Soil Type", title="Relação entre Temperatura e Umidade por Tipo de Solo")
        st.plotly_chart(fig)

        # Gráfico 2: Distribuição de Nitrogênio, Potássio e Fósforo
        st.write("### Distribuição de Nutrientes no Solo")
        nutrients = filtered_df[["Nitrogen", "Potassium", "Phosphorous"]]
        fig = px.bar(nutrients, title="Distribuição de Nitrogênio, Potássio e Fósforo")
        st.plotly_chart(fig)

        # Gráfico 3: Contagem de Tipos de Cultura
        st.write("### Contagem de Tipos de Cultura")
        crop_counts = filtered_df["Crop Type"].value_counts()
        fig = px.pie(values=crop_counts, names=crop_counts.index, title="Distribuição de Tipos de Cultura")
        st.plotly_chart(fig)

        # Gráfico 4: Relação entre Umidade e Teor de Nitrogênio
        st.write("### Relação entre Umidade e Teor de Nitrogênio")
        fig = px.scatter(filtered_df, x="Humidity", y="Nitrogen", trendline="ols", title="Relação entre Umidade e Nitrogênio")
        st.plotly_chart(fig)

else:
    st.info("Por favor, faça upload de um arquivo CSV para começar a análise.")
