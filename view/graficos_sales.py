
import pandas as pd
import plotly.express as px
import streamlit as st

st.title("sales1")

#parte1

sales = "sales.xlsx"
df_sales = pd.read_excel(sales)



#parte 3 a

df_sales["Data venda"] = pd.to_datetime(df_sales["Data venda"])

#isolanado o doa do campo"data venda
df_sales["Dia"] = df_sales["Data venda"].dt.day

#parte2
st.write("mostrando o frontend")
st.dataframe(df_sales)
