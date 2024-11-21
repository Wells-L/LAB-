
import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Informações de vendas")

#parte1

sales = "sales.xlsx"
df_sales = pd.read_excel(sales)

#parte2
st.write("Dados de venda")
st.dataframe(df_sales)

#parte 3 trartativa 1
st.title("receita por dia")
df_sales["Data venda"] = pd.to_datetime(df_sales["Data venda"])

#isolanado o dia do campo data venda
df_sales["Dia"] = df_sales["Data venda"].dt.day

#tratativa 2 
df_sales = df_sales.loc[df_sales["Status"] == "Finalizado"]

#tratativa 3
df_sales = df_sales.loc[df_sales["Consultor"] != "BKO Vendas"]
st.dataframe(df_sales)
#groupby vendas por dia

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

#vendas por dia de cada loja

st.title("vendas por dia de cada loja")


grafico_vendas_dia_loja = (
    df_sales
    .groupby(["Dia", "Unidade"])
    .agg({"Valor líquido": "sum"})
    .reset_index()
  )

grafico_vendas_dia_loja = px.bar(
      grafico_vendas_dia_loja,
      x="Dia",
      y="Valor líquido",
      color="Unidade",

)

st.plotly_chart(grafico_vendas_dia_loja)

#profissoes que mais compram
#dividir em duas colonas col1, col2 = st.column(2)

st.title("profissões que mais compram")

grafico_profissao_compra = (
    df_sales
    .groupby("Profissão cliente")
    .agg({"Valor líquido": "sum"})
    .reset_index()
  )#sort_values(valor liquido", ascending=False)

grafico_profissao_compra = px.bar(
      grafico_profissao_compra,
      x="Profissão cliente",
      y="Valor líquido",
      labels={"Valor líquido":"Valor","Profissão cliente":"Profissão"}
)

st.plotly_chart(grafico_profissao_compra)

#profissoes que mais compram grafico de pizza


#Consultor que mais vendeu



st.title("Consultor que mais vendeu")

grafico_Consultor_vendas = (
      df_sales
      .groupby("Consultor")
      .agg({"Valor líquido": "sum"})
      .reset_index()
)

grafico_Consultor_vendas = px.bar(
      grafico_Consultor_vendas,
      x="Consultor",
      y="Valor líquido",
      labels={"Valor líquido":"Valor","Consultor":"Consultor"}
)

st.plotly_chart(grafico_Consultor_vendas)

#procedimento que mais vendeu

st.title("procedimento que mais vendeu")

grafico_procedimento_vendas = (
      df_sales
      .groupby("Procedimento")
      .agg({"Valor líquido": "sum"})
      .reset_index()
)

grafico_procedimento_vendas = px.bar(
      grafico_procedimento_vendas,
      x="Procedimento",
      y="Valor líquido",
      labels={"Valor líquido":"Valor","Procedimento":"Procedimento"}
)

st.plotly_chart(grafico_procedimento_vendas)


#tabela
