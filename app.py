import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Launch Cadency Visualizator", layout="wide")

# US-01: Título e descrição do projeto
st.header("Welcome to Launch Cadency Visualizator")
st.text("Launch Cadency Visualizator (VCS) is a program made to track all rocket launches since 1995 until 2020.")
st.text("All dashboards in this app, gives a complete view about the today's astronautic cenarious and how it's been changing. Enjoy it!")

# US-02: Mostrar dataframe
# Ler arquivo
# converter arquivo para objeto dataframe pandas
pandas_dataframe = pd.read_csv('space.csv')

# mostrar objeto dataframe em um dataframe do streamlit
st.dataframe(pandas_dataframe)

# Salvar no github