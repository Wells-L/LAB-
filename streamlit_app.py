
import os
import shutil
import subprocess
import pandas as pd
import os
import requests
import json
import streamlit as st
import pandas as pd


# side bar para selecao de paginas
st.sidebar.title("menu do Lucas")
page = st.sidebar.selectbox("escolha uma pagina",["Calculadora","Conversor","testes","testes2","graficos","forca"])

if page == "Calculadora":

  #pagina de calculadora
  st.title("Calculadora")

  st.write("Faça a sua conta")



  numero_1 = st.text_input("digite um numero")
  numero_2 = st.text_input("digite outro numero")



  operacao = st.selectbox("Escolha a operação", ["soma", "subtração","divisão","potenciação","raiz quadrada"])
  resultado = None

  if numero_1 and numero_2:

    if operacao == "soma":

      resultado = float(numero_1) + float(numero_2)
      st.write(f"A soma dos numeros é : {resultado}")

    elif operacao == "subtração":

      resultado = float(numero_1) - float(numero_2)
      st.write(f"A subtração dos numeros é : {resultado }")

    elif operacao == "multiplicação":

      resultado = float(numero_1) * float(numero_2)
      st.write(f"A multiplicação dos numeros é : {resultado }")

    elif operacao == "divisão":

      resultado = float(numero_1) / float(numero_2)
      st.write(f"A divisao dos numeros é : {resultado }")

    elif operacao == "potenciação":

      resultado = float(numero_1) ** float(numero_2)
      st.write(f"A potenciação dos numeros é : {resultado }")

    elif operacao == "raiz quadrada":

      resultado = sqrt(float(numero_1))
      st.write(f"A raiz quadrada dos numeros é : {resultado }")


elif page == "Conversor":

  st.title("Conversor")

  real_amount = st.text_input("Enter the amount in real (R$):")
  exchange_rate = 0.20

  if real_amount:
    try:
      real_value = float(real_amount)
      dollar_value = real_value * exchange_rate
      st.write(f"Result: ${dollar_value:.2f}")
    except ValueError:
      st.write("Invalid input. Please enter a valid number.")



elif page == "testes":

  st.title("Conversor 2")
  moeda = st.selectbox("Moeda", ["real", "dolar"])


  valor_real_para_dolar = 5.45


  if moeda == "dolar":
    numero_dolar = st.number_input("Insira um valor em Dólar para real")
    resultado = numero_dolar * valor_real_para_dolar
    st.write(f"O resultado é: R$ {resultado:.2f}")

  elif moeda == "real":
    numero_real = st.number_input("Insira um valor em Real para Dólar")
    resultado = numero_real / valor_real_para_dolar
    st.write(f"O resultado é: USD {resultado:.2f}")


elif page == "testes2":

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

elif page == "graficos":

  st.title("Graficos")

  leads = 'leads.xlsx'
  df_leads = pd.read_excel(leads)

  st.dataframe(df_leads)


elif page == "forca":

  st.title("bem vindo ao jogo da forca")  

  st.write(f"A palavra tem {len(st.session_state.palavra_secreta)} letras.")
  st.write(" ".join(st.session_state.palavra_chutada))

