import streamlit as st
import pandas as pd
import os

# PANDAS CONFIGURAÇÃO DATAFRAME (Projeção)

# Ler e converter arquivo para objeto dataframe pandas
launch_df = pd.read_csv('space.csv')


# 1. Limpa os nomes das colunas (remove espaços em branco antes e depois)
launch_df.columns = launch_df.columns.str.strip()

# 2. Converte a coluna de data para o formato datetime e lida com o 'UTC'
launch_df['Launch date'] = pd.to_datetime(launch_df['Launch date'].str.replace('UTC', '').str.strip(), errors='coerce')

# 3. Cria uma nova coluna 'Year' extraindo o ano da data de lançamento
launch_df['Year'] = launch_df['Launch date'].dt.year

# 4. deletando coluna rocket pois eu não uso
launch_df = launch_df.drop(columns={"Rocket"})

# Mostrando colunas df
#print(launch_df.columns)
print("")
# tipo de dados utilizado na tabela
#print(launch_df.dtypes)

# STREAMLIT
st.set_page_config(page_title="Launch Cadency Visualizator", layout="wide")

# US-01: Título e descrição do projeto
st.header("Welcome to Launch Cadency Visualizator")
st.text("Launch Cadency Visualizator (VCS) is a program made to track all rocket launches since 1995 until 2020.")
st.text("All dashboards in this app, gives a complete view about the today's astronautic cenarious and how it's been changing. Enjoy it!")

# US-02: Mostrar dataframe
st.dataframe(launch_df, hide_index=True)

# US-03: Mostrar grafico de barra compara número de lançamento (eixo Y) por ano (eixo X)

# Temos que agrupar os lançamentos pela coluna Year. E essa coluna Year se transformará nos index dos grupos
# 2018: 10; 2019: 20; 2020: 30

# Agrupando linhas por ano, contando Ids presentes em cada ano e colocando na coluna de Launch Count
launches_per_year_df = launch_df.groupby("Year")['Id'].count().reset_index(name='Launch Count')
launches_per_year_df["Year"] = launches_per_year_df["Year"].astype(int)

# Como usuário, quero ter um filtro de slider para selecionar um intervalo de anos e ver os dados apenas para esse período

value = st.slider(label="Filtro por ano", min_value=1957, max_value=2020)

# Agora de acordo com o ano, eu deleto todos os anos anteriores ao que está selecionado no slider

filtered_launches_per_year_df = launches_per_year_df[launches_per_year_df["Year"] >= value]

st.line_chart(filtered_launches_per_year_df, x="Year", y="Launch Count", color="#03BB40")

