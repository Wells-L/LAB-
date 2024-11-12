
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

col1,col2 = st.columns(2)

with col1 :


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

with col2 :

  groupby_leads_por_unidade = (
    df_leads
    .groupby("Unidade")
    .agg({"ID do lead": "nunique"})
    .reset_index()
  )


  grafico_leads_por_unidade = px.bar(
      groupby_leads_por_unidade,
      x="Unidade",
      y="ID do lead",
      labels={"ID do lead": "Quantia de Leads", "Unidade":"Unidade"},

  )

  st.plotly_chart(grafico_leads_por_unidade)



  st.write("grafico por unidade")


##############################################################

col3,col4 = st.columns(2)
#groupby 4 c
with col3 :

  groupby_leads_por_fonte = (
  df_leads
  .groupby("Fonte")
  .agg({"ID do lead": "nunique"})
  .reset_index()
)
   #grafico


  grafico_leads_por_fonte = px.pie(
    groupby_leads_por_fonte,
    names="Fonte",
    values="ID do lead",
    title = "número de leads por fonte",
    labels={"ID do lead": "Quantia de Leads", "Fonte":"Fonte"},
)
  st.plotly_chart(grafico_leads_por_fonte)

with col4 :

  groupby_leads_por_Status = (
  df_leads
  .groupby("Status")
  .agg({"ID do lead": "nunique"})
  .reset_index()
)



  grafico_leads_por_Status = px.pie(
    groupby_leads_por_Status,
    names="Status",
    values="ID do lead",
    title = "número de leads por fonte",
    labels={"ID do lead": "Quantia de Leads", "Status":"Status"},
)
  st.plotly_chart(grafico_leads_por_fonte)
