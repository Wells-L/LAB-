
import pandas as pd
import plotly.express as px
import streamlit as st

leads = "leads.xlsx"
df_leads = pd.read_excel(leads)

st.write("dataframe")
st.dataframe(df_leads)

df_leads["dia da entrada"] = pd.to_datetime(df_leads["Dia de entrada"])
df_leads["dia"] = df_leads["dia de entrada"].dt.day

groupby_leads_por_dia = df_leads.groupby("dia").agg({"ID do lead": "nunique}"}).reset_index

st.write("graficos de leads por dia")

grafico_leads_por_dia = px.line(
    groupby_leads_por_dia,
    x="",
    y="",
    labels={"ID do dia": "Quantia de Leads", "Dia":"Dia do mês"},
    markers=True
)

st.plotly_chart(grafico_leads_por_dia)
