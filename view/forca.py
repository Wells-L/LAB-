
#imports
import random
import streamlit as st
from unidecode import unidecode



#título
st.title("FORCA1")

# escolhendo palavra
lista_palavras = []
with open('content/palavras.txt', 'r') as palavras_file:
    for line in palavras_file:
        lista_palavras.append(line.strip())

if "palavra_secreta" in st.session_state:
  pass
else:
  st.session_state["palavra_secreta"] = unidecode(random.choice(lista_palavras))
palavra_secreta = st.session_state["palavra_secreta"]

#colocando as letras chutadas

if "letras_chutada" in st.session_state:
  pass
else:
  st.session_state["letras_chutada"] = ["_" for letra in palavra_secreta]

letras_chutada = st.session_state["letras_chutada"]
st.title(" ".join(letras_chutada))


if "letras_tentadas" in st.session_state:

  pass
else:
  st.session_state["letras_tentadas"] = []
letras_tentadas = st.session_state["letras_tentadas"]




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
  st.session_state["tentativas"] = len(palavra_secreta)
tentativas =  st.session_state["tentativas"]

if "verificar_chute" in st.session_state:
  pass
else:
  st.session_state["verificar_chute"] = False
verificar_chute = st.session_state["verificar_chute"]


#lógica
st.write(tentativas)

if st.button("chutar"):
  if chute in letras_tentadas:
    verificar_chute = True

  else:
    letras_tentadas.append(chute)
    acertou = False
    verificar_chute = False
    for index, letra in enumerate(palavra_secreta):
      if chute == letra:
        letras_chutada[index] = letra
        acertou = True
        acertos += 1
  

    if acertou == False:
      tentativas -= 1


  st.write(f"Letras tentadas: {', '.join(letras_tentadas)}")

  st.session_state["acertos"] = acertos
  st.session_state["acertou"] = acertou
  st.session_state["tentativas"] = tentativas
  st.session_state["verificar_chute"] = verificar_chute 
  st.session_state["letras_tentadas"] = letras_tentadas
  st.rerun()
# mensagens
if acertou == False:
  st.write("essa letra não esta na palavra")
  st.write(f"você possui mais {tentativas} tentativas restantes")

if verificar_chute == True:
  st.write("voce ja tentou esta letra, por favor tente outra")


if acertos == len(palavra_secreta):

  st.write("Parabens você ganhou")
  st.balloons()
if tentativas == 0:
  st.write(f"você perdeu a palavra era: {palavra_secreta}")

st.write(f"essas sao as suas letras tentadas{", ".join(letras_tentadas)}")

st.session_state["letras_chutada"] = letras_chutada

@st.dialog("selecione sua dificuldade")
def dificuldade():
    st.write(f"selecione a sua dificuldade")
    dificuldade = st.selectbox("Escolha o nível de dificuldade:", ("Fácil", "Médio", "Difícil"))
    if st.button("Submit"):

        st.session_state["palavra_secreta"] = unidecode(random.choice(lista_palavras))
        palavra_secreta = st.session_state["palavra_secreta"]
        st.session_state["letras_chutada"] = ["_" for letra in palavra_secreta]
        st.session_state["acertos"] = 0
        st.session_state["letras_tentadas"] = []

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


