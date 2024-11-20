
import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Informações de vendas3")

#parte1

sales = "sales.xlsx"
df_sales = pd.read_excel(sales)

#parte2
st.write("Dados de venda")
st.dataframe(df_sales)

#parte 3 a
st.title("receita por dia")
df_sales["Data venda"] = pd.to_datetime(df_sales["Data venda"])

#isolanado o doa do campo"data venda
df_sales["Dia"] = df_sales["Data venda"].dt.day

#parte4 groupby vendas por dia

groupby_vendas_por_dia = (
    df_sales
    .groupby("Dia")
    .agg({"Valor líquido": "sum"})
    .reset_index()
  )

grafico_vendas_por_dia = px.bar(
      groupby_vendas_por_dia,
      x="Dia",
      y="Valor líquido",
      labels={"Valor líquido": "Valor", "Dia":"Dia"},

  )

st.plotly_chart(grafico_vendas_por_dia)

st.write("mostrando vendas por dia ")
st.dataframe(groupby_vendas_por_dia)

#parte5

grafico_vendas_dia_loja = (
    df_sales
    .groupby("Dia, Unidade")
    .agg({"Valor líquido": "sum"})
    .reset_index()
  )


#profissao que mais compra
#consultor que mais vendeu
#procedimento que mais vendi
