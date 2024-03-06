import numpy as np
import pandas as pd
import plotly_express as px
import streamlit as st

st.set_page_config(
    page_title="BBC_Extratos",
    page_icon=':bar_chart:',
    layout='wide',
    initial_sidebar_state='collapsed'
)


# st.markdown(
#     """
#     # Titulo com markdown
#     ## subtitulo
#     > Texto
#     *Italico*
#     **Negrito**
#     ``` Select * FROM alguma coisa ```
# """
# )

dataframe = pd.read_csv('Linda.csv')
year = st.sidebar.multiselect(
    key=1,
    label="Year",
    options=dataframe["Year"].unique(),
    default=dataframe["Year"].unique(),
)

month = st.sidebar.multiselect(
    key=2,
    label="Month",
    options=dataframe["Month"].unique(),
    default=dataframe["Month"].unique(),
)

descricao = st.sidebar.multiselect(
    key=3,
    label="Descrição",
    options=dataframe["Descrição"].unique(),
    default=dataframe["Descrição"].unique(),
)

dataframe = dataframe.query("Year == @year and Month == @month and Descrição == @descricao")

st.header(":bar_chart: BBC_Extrato")
st.markdown('#')

Total_Rx_Lucht =round(dataframe['Valor'].sum(), 2)
Total_items = len(dataframe["Descrição"].unique())

RX_LUCHT_by_months = (
    dataframe.groupby(by="Month").sum(numeric_only=True)[["Valor"]].sort_values("Month")
)

fig_RX_LUCHT_by_date = px.area(
    RX_LUCHT_by_months,
    title="<b>RX_LUCHT By Order Date</b>",
    x=RX_LUCHT_by_months.index,
    y="Valor",
    orientation="v",
    color_discrete_sequence=["#FF4B4B"] * len(RX_LUCHT_by_months),
)

st.plotly_chart(fig_RX_LUCHT_by_date)

col1, col2 = st.columns([0.3, 0.7])


col1.metric("Total_Rx_Lucht", Total_Rx_Lucht)
col2.metric("Total_items", Total_items)

st.markdown('''----''')



st.dataframe(dataframe)
