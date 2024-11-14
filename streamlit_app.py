
import os
import shutil
import subprocess
import pandas as pd
import os
import requests
import json
import streamlit as st
import pandas as pd
import plotly.express as px

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

conversor = st.Page(
    "view/conversor.py",
    title="valores",
    icon="🪙",
)

graficos = st.Page(
    "view/graficos.py",
    title="gráficos",
    icon="📊",
)

#configuracao da navegação
pg = st.navigation(
    {
        "parte 1":[calculadora],
        "item 2":[forca],
        "item 3":[conversor],
        "item4":[graficos]

    }
)

graficos_sales = st.Page(
    "view/graficos_sales.py",
    title="Sales",
    icon="💸",
)

pg.run()
