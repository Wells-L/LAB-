
import pandas as pd
import plotly.express as px
import streamlit as st
#parte 1 
st.title("graficos")
#parte 2
leads = "leads.xlsx"
df_leads = pd.read_excel(leads)
#parte 3
st.write("dataframe")
st.dataframe(df_leads)

df_leads["Dia da entrada"] = pd.to_datetime(df_leads["Dia da entrada"])
df_leads["Dia"] = df_leads["Dia da entrada"].dt.day

groupby_leads_por_dia = df_leads.groupby("Dia").agg({"ID do lead": "nunique"}).reset_index()

st.write("graficos de leads por dia")

grafico_leads_por_dia = px.line(
    groupby_leads_por_dia,
    x="Dia",
    y="ID do lead",
    labels={"ID do lead": "Quantia de Leads", "Dia":"Dia do mês"},
    markers=True
)

st.plotly_chart(grafico_leads_por_dia)

#################################################
#grafico de barras



groupby_leads_por_unidade = (
  df_leads
  .groupby("Unidade")                  
  .agg({"ID do lead": "nunique"})
  .reset_index()
)  


grafico_leads_por_unidade = px.bar(
    groupby_leads_por_dia,
    x="Dia",
    y="ID do lead",
    labels={"ID do lead": "Quantia de Leads", "Dia":"Dia do mês"},
    markers=True
)

st.plotly_chart(grafico_leads_por_unidade)



st.write("grafico por unidade")
