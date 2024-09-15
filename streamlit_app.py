
import streamlit as st
import math as mt
from math import sqrt

# side bar para selecao de paginas
st.sidebar.title("menu do Lucas")
page = st.sidebar.selectbox("escolha uma pagina",["Calculadora","Conversor"])

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
