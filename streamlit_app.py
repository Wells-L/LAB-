
import streamlit as st
import math as mt
from math import sqrt
import requests
import json

# side bar para selecao de paginas
st.sidebar.title("menu do Lucas")
page = st.sidebar.selectbox("escolha uma pagina",["Calculadora","Conversor","testes","testes2"])

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



elif page == "testes ":

  st.title("Conversor 2")
  moeda = st.selectbox("Moeda",["real","dolar"])

  valor_real = 5.48
  valor_dolar = 1.00




  if moeda == "dolar":

    numero_dolar = st.number_input("insira um valor em Dolar PARA REAL")
    resultado = (numero_dolar * valor_dolar)
    st.write(f"o Resultado é : R${resultado}")



  elif moeda == "real":
    numero_real = st.number_input("insira um valor em real PARA DOLAR")
   
    resultado = (numero real * valor_real)

    st.write(f"o Resultado é : USD {resultado}")




  url = "https://api.exchangerate-api.com/v4/latest/USD"
  my_resquest = requests.get(url)

  content = my_resquest.content
  dados = json.loads(content)

  dados['rates']["BRL"]

  taxa_de_conversao = (dados['rates']["BRL"])



elif page == "testes2":

  url = "https://api.exchangerate-api.com/v4/latest/USD"
  my_resquest = requests.get(url)

  content = my_resquest.content
  dados = json.loads(content)

  dados['rates']["BRL"]

  taxa_de_conversao = (dados['rates']["BRL"])
  taxa_conversao_dolar =  (dados['rates']["USD"])/(dados['rates']["BRL"])


  st.title("Conversor 3")
  moeda = st.selectbox("Moeda",["real","dolar"])


  valor_do_dolar_para_real = (dados['rates']["BRL"])
  valor_do_real_para_dolar = (dados['rates']["USD"])/(dados['rates']["BRL"])



  if moeda == "dolar":

    numero_dolar = st.number_input("insira um valor em Dolar PARA REAL")
    resultado = (numero_dolar * valor_do_dolar_para_real)
    st.write(f"o Resultado é : R${resultado}")



  elif moeda == "real":
    numero_real = st.number_input("insira um valor em real PARA DOLAR")
    resultado = (numero_real * valor_real)

    st.write(f"o Resultado é : USD {resultado}")



