
import streamlit as st
import os
import shutil
import subprocess
import pandas as pd
import os
import requests
import json
import pandas as pd


url = "https://api.exchangerate-api.com/v4/latest/USD"
my_resquest = requests.get(url)

content = my_resquest.content
dados = json.loads(content)
lista_moeda = list(dados['rates'].keys())

col_1,col_2 = st.columns(2)

with col_1:

  moeda_1 = st.selectbox("Moeda 1", lista_moeda)
  moeda_2 = st.selectbox("Moeda 2", lista_moeda)

  conversao_moeda_1 = dados['rates'][moeda_1]
  conversao_moeda_2 = dados['rates'][moeda_2]


  numero = st.number_input("digite um valor")


with col_2:
  st.write("Resultado")

  valor_convertido = ( numero * conversao_moeda_2)/conversao_moeda_1
  st.write(f"O resultado é: {valor_convertido:.2f}")
