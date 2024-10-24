
import pandas as pd
import plotly.express as px
import streamlit as st

leads = "leads.xlsx"
df_leads = pd.read_excel(leads)

st.write("dataframe")
st.dataframe(df_leads)
