
import random
import streamlit as st

st.title("forca_teste3")


lista_palavras = []
with open('content/palavras.txt', 'r') as palavras_file:
    for line in palavras_file:
        lista_palavras.append(line.strip())

if "palavra_secreta" in st.session_state:
  pass
else:
  st.session_state["palavra_secreta"] = random.choice(lista_palavras)

palavra_secreta = st.session_state["palavra_secreta"]

st.write(palavra_secreta)

if "letras_chutada" in st.session_state:
  pass
else:
  st.session_state["letras_chutada"] = ["_" for letra in palavra_secreta]

letras_chutada = st.session_state["letras_chutada"]
st.title(" ".join(letras_chutada))

chute = st.text_input("Escolha uma letra: ")

acertou = False
acertos = 0
tentativas = len(palavra_secreta)
# trazer as variasveis todas abaixo do click do botão
 # declarar palavras chutadas e armazenar os acertos e tentativas


if st.button("chutar"):
  st.write(palavra_secreta) 
  for index, letra in enumerate(palavra_secreta):
    if chute == letra:
      letras_chutada[index] = letra
      acertou = True
      acertos += 1 
    else:
      
      tentativas - 1
  if acertou == False:
    st.write("essa letra nao esta na palavra")
  if acertos == len(palavra_secreta):

    st.write("Parabens voce ganhou")

  if tentativas == 0:
    st.write(f"voce perdeu a palavra era: {palavra_secreta}")
  st.rerun()
  
st.session_state["letras_chutada"] = letras_chutada

if st.button("mudar palavra"):
  st.session_state["palavra_secreta"] = random.choice(lista_palavras)
  palavra_secreta = st.session_state["palavra_secreta"]
  st.session_state["letras_chutada"] = ["_" for letra in palavra_secreta]

  st.balloons()

  st.rerun()


