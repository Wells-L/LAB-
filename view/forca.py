
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

letras_chutada = ["_" for letra in palavra_secreta]
st.title(" ".join(letras_chutada))

chute = st.text_input("Esolha uma letra: ")

if st.button("chute: "):
  
  for index, letra in enumerate(palavra_secreta):
    if chute == letra:
      letras_chutada [index] = letra

      st.write(" ".join(letras_chutada))
    else:
      st.write("essa letra nao esta na palavra")
     


if st.button("mudar palavra"):
  st.session_state["palavra_secreta"] = random.choice(lista_palavras)
  st.balloons()

for index, letra in enumerate(palavra_secreta):
    if chute == letra:
      palavra_chutada [index] = letra

      print("Boa! Você acertou uma letra.")
    else:
      num_tentativas -= 1
      print(f"A letra '{chute}' não está na palavra.")

