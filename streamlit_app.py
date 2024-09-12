
import streamlit as st

st.title("Calculadora Skibidi")

st.write("calculadora que faz meuneng 24 dias po hora")


numero_1 = st.text_input("digite um numero")

st.write(f"O numero escrito é : {numero_1}")

numero_2 = st.text_input("digite outro numero")

st.write(f"O numero escrito é : {numero_2}")
operacao = st.selectbox("Escolha a operação", ["soma", "subtração", "multiplicação", "divisão"])

if numero_1 and numero_2:
  soma = int(numero_1) + int(numero_2)
  st.write(f"A soma dos numeros é : {soma}")



  operacao = input("digite a operação que deseja realizar: ")


if operacao == "+" or operacao == "soma":

  num_1 = input("digite um numero")

  num_2 = input("digite outro numero")

  soma = int(num_1) + int(num_2)

  print(f"a soma entre os numeros é {soma}")

elif operacao == "-" or operacao == "subtração":
  
  num_1 = input("digite um numero")
  
  num_2 = input("digite outro numero")

  subtracao = int(num_1) - int(num_2)

  print(f"a subtração entre os numeros é {subtracao}")

elif operacao == "*" or operacao == "multiplicação":

  num_1 = input("digite um numero")

  num_2 = input("digite outro numero")

  multiplicacao = int(num_1) * int(num_2)

  print(f"a multiplicação entre os numeros é {multiplicacao}")

elif operacao == "/"or operacao == "divisão":

  num_1 = input("digite um numero")

  num_2 = input("digite outro numero")

  divisao = int(num_1) / int(num_2)

  print(f"a divisão entre os numeros é {divisao}")


elif operacao == "**" or operacao == "potenciação" or operacao == "potência":

  num_1 = input("digite um numero")
  
  num_2 = input("digite outro numero")

  potencia = int(num_1) ** int(num_2)

  print(f"a potenciação entre os numeros é {potencia}")
