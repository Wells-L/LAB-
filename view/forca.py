
#imports
import random
import streamlit as st
import unicodedata

def remove_acentos(input_str):
    # Normalize the string to decompose accent characters
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    # Filter out combining characters (accents) by keeping only ASCII characters
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])


#título
st.title("FORCA4")

# escolhendo palavra
lista_palavras = []
with open('content/palavras.txt', 'r') as palavras_file:
    for line in palavras_file:
        lista_palavras.append(line.strip())

if "palavra_secreta" in st.session_state:
  pass
else:
  st.session_state["palavra_secreta"] = remove_acentos(random.choice(lista_palavras))
palavra_secreta = st.session_state["palavra_secreta"]

#colocando as letras chutadas

if "letras_chutada" in st.session_state:
  pass
else:
  st.session_state["letras_chutada"] = ["_" for letra in palavra_secreta]

letras_chutada = st.session_state["letras_chutada"]
st.title(" ".join(letras_chutada))






st.write(palavra_secreta)
# chute
chute = st.text_input("Escolha uma letra: ")

#contador de acertos e tentativas

if "acertou" in st.session_state:
  pass
else:
  st.session_state["acertou"] = False
acertou =  st.session_state["acertou"]

if "acertos" in st.session_state:
  pass
else:
  st.session_state["acertos"] = 0
acertos = st.session_state["acertos"]
#st.write(f"acertos :{acertos}")
if "tentativas" in st.session_state:
  pass
else:
  st.session_state["tentativas"] = tentativas_totais
tentativas =  st.session_state["tentativas"]

#lógica
st.write(tentativas)

if st.button("chutar"):
  st.write(palavra_secreta)
  acertou = False
  for index, letra in enumerate(palavra_secreta):
    if chute == letra:
      letras_chutada[index] = letra
      acertou = True
      acertos += 1
  if acertou == False:
    tentativas -= 1

  st.session_state["acertos"] = acertos
  st.session_state["acertou"] = acertou
  st.session_state["tentativas"] = tentativas

  st.rerun()

if acertou == False:
  st.write("essa letra nao esta na palavra")
  st.write(f"voce possui mais {tentativas} tentativas restantes")

if acertos == len(palavra_secreta):

  st.write("Parabens voce ganhou")
  st.balloons()
if tentativas == 0:
  st.write(f"voce perdeu a palavra era: {palavra_secreta}")

st.session_state["letras_chutada"] = letras_chutada

@st.dialog("selecione sua dificuldade")
def dificuldade():
    st.write(f"selecione a sua dificuldade")
    dificuldade = st.selectbox("Escolha o nível de dificuldade:", ("Fácil", "Médio", "Difícil")) 
    if st.button("Submit"):

        st.session_state["palavra_secreta"] = remove_acentos(random.choice(lista_palavras))
        palavra_secreta = st.session_state["palavra_secreta"]
        st.session_state["letras_chutada"] = ["_" for letra in palavra_secreta]
        st.session_state["acertos"] = 0

        if dificuldade == "Fácil":
            tentativas_totais = len(palavra_secreta) + 3
        elif dificuldade == "Médio":
            tentativas_totais = len(palavra_secreta)
        elif dificuldade == "Difícil":
            tentativas_totais = len(palavra_secreta) - 2

        st.session_state["tentativas"] = tentativas_totais
        st.session_state["acertou"] = True

        st.rerun()

if st.button("mudar palavra"):

  dificuldade()

#arrumar tentativas
#colocar função do enter
