
import random
import streamlit as st

st.title("forca")


lista_palavras = []
with open('content/palavras.txt', 'r') as palavras_file:
    for line in palavras_file:
        lista_palavras.append(line.strip())


palavra_secreta = random.choice(lista_palavras)

st.write(palavra_secreta)


chute = st.text_input("Esolha uma letra: ")

if st.button("chute: "):
  st.write(chute)

