
import os
import shutil
import subprocess
import pandas as pd
import os
import requests
import json
import streamlit as st
import pandas as pd

#configuracao da pagina

calculadora = st.Page(
    "view/calculadora.py",
    title="calculadora",
    icon="🧮",
)

forca = st.Page(
    "view/forca.py",
    title="jogo da forca",
    icon="💀",
)

Conversor = st.Page(
    "view/forca.py",
    title="jogo da forca",
    icon="💀",
)

graficos = st.Page(
    "view/forca.py",
    title="jogo da forca",
    icon="💀",
)


#configuracao da navegação
pg = st.navigation(
    {
        "parte1":[calculadora],
        "item2":[forca],
    }
)

pg.run()
