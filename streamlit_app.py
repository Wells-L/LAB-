
import streamlit as st

st.title("Hello World!")

st.write("sou o Lucas")


numero_1 = st.text_input("digite um numero")

st.write(f"O numero escrito é : {numero_1}")

numero_2 = st.text_input("digite outro numero")

st.write(f"O numero escrito é : {numero_2}")
operacao = st.selectbox("Escolha a operação", ["soma", "subtração", "multiplicação", "divisão"])

if numero_1 and numero_2: 
  soma = int(numero_1) + int(numero_2)
  st.write(f"A soma dos numeros é : {soma}")
