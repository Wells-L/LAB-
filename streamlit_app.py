
import streamlit as st

st.title("Calculadora Skibidi")

st.write("calculadora que faz meuneng 24 dias po hora")


numero_1 = st.text_input("digite um numero")

st.write(f"O numero escrito é : {numero_1}")

numero_2 = st.text_input("digite outro numero")

st.write(f"O numero escrito é : {numero_2}")
operacao = st.selectbox("Escolha a operação", ["soma", "subtração", "multiplicação", "divisão"])

if operacao == "soma":
  soma = int(numero_1) + int(numero_2)
  st.write(f"A soma dos numeros é : {soma}")


