
import random
import streamlit as st

st.title("forca")


lista_palavras = []
with open('content/palavras.txt', 'r') as palavras_file:
    for line in palavras_file:
        lista_palavras.append(line.strip())


palavra_secreta = random.choice(lista_palavras)
st.title("forca")
st.write(palavra_secreta)

if st.button("teste"):
  st.write("Botão clicado!")

if "contador" not in st.session_state:
  st.session_state["contador"] = 0

if st.button("somar"):
  st.session_state["contador"] += 1
st.write(f"o seu contador é igual a: {st.session_state["contador"]}")

if st.button("resetar"):
  st.session_state["contador"] = 0
