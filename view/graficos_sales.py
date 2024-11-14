
import pandas as pd
import plotly.express as px
import streamlit as st

st.title("sales1")

#parte1

sales = "sales.xlsx"
df_sales = pd.read_excel(sales)

#parte2
st.write("mostrando o frontrend")
st.dataframe(df_sales)
