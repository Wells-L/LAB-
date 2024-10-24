
import random
import streamlit as st

st.title("forca")


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

chute = st.text_input("Esolha uma letra: ")

acertou = False

if st.button("chutar"):

  for index, letra in enumerate(palavra_secreta):
    if chute == letra:
      st.session_state["letras_chutada"] [index] = letra
     
      acertou = True
  else:
    acertou = False
    st.write("essa letra nao esta na palavra")



if st.button("mudar palavra"):
  st.session_state["palavra_secreta"] = random.choice(lista_palavras)
  palavra_secreta = st.session_state["palavra_secreta"]
  st.session_state["letras_chutada"] = ["_" for letra in palavra_secreta]

  st.balloons()


