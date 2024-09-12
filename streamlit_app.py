
import streamlit as st

st.title("Calculadora")

st.write("Faça a sua conta")


numero_1 = st.text_input("digite um numero")

st.write(f"O numero escrito é : {numero_1}")

numero_2 = st.text_input("digite outro numero")

st.write(f"O numero escrito é : {numero_2}")

operacao = st.selectbox("Escolha a operação", ["soma", "subtração", "multiplicação", "divisão"])

if operacao == "soma":

  soma = float(numero_1) + float(numero_2)
  st.write(f"A soma dos numeros é : {soma}")

elif operacao == "subtração":

  subtração = float(numero_1) - float(numero_2)
  st.write(f"A subtração dos numeros é : {subtração }")

elif operacao == "multiplicação":

  multiplicação = float(numero_1) * float(numero_2)
  st.write(f"A multiplicação dos numeros é : {multiplicação }")

elif operacao == "divisão":

  divisão = float(numero_1) / float(numero_2)
  st.write(f"A divisão dos numeros é : {divisão }")







