
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

#configuracao da navegação 
pg = st.navigation(
    {
        "parte1":[calculadora],
    }
)

pg.run()
