import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="Govt. Funding💵",
                   page_icon="💵",
                   )


df_sam_sik=pd.read_csv(f'funds/Year-wise Funds Disbursed for Teacher Training under Samagra Shiksha from 2018-19 to 2020-21.csv')




fig_sam_sik = go.Figure(data=[go.Table(
    header=dict(values=list(df_sam_sik.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=14, color="black"),
                align='left'),
    cells=dict(values=df_sam_sik.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=14, color="black"),
               align='left'))
])
# Add fig_subure title
fig_sam_sik.update_layout(
    title_text="Year-wise Funds Disbursed for Teacher Training under Samagra Shiksha from 2018-19"
)
st.plotly_chart(fig_sam_sik)



df_fin_sup=pd.read_csv(f'funds/StateUT-wise Approved Financial Support to the Teachers (Elementary and Secondary Schools) under Samagra Shiksha during 2021-22.csv')

df_fin_sup=df_fin_sup.drop('Sl. No.', axis=1)


fig_fin_sup = go.Figure(data=[go.Table(
    header=dict(values=list(df_fin_sup.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=14, color="black"),
                align='left'),
    cells=dict(values=df_fin_sup.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=14, color="black"),
               align='left'))
])
# Add fig_subure title
fig_fin_sup.update_layout(
    title_text="Apprvd Fin. Support for Teachers(Elementary/Secondary Schools)by Samagra Shiksha(2021-22)",
     autosize=False,
    width=1000,
    height=1000,
    xaxis=go.layout.XAxis(linecolor="black", linewidth=1, mirror=True),
    yaxis=go.layout.YAxis(linecolor="black", linewidth=1, mirror=True),
    margin=go.layout.Margin(l=50, r=50, b=100, t=100, pad=4),
)
st.plotly_chart(fig_fin_sup)




df_fin_Expen=pd.read_csv(f'funds/Year-wise Details of Expenditure incurred on Teacher Training under Samagra Shiksha from 2018-19 to 2022-23.csv')




fig_fin_Expen = go.Figure(data=[go.Table(
    header=dict(values=list(df_fin_Expen.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=14, color="black"),
                align='left'),
    cells=dict(values=df_fin_Expen.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=14, color="black"),
               align='left'))
])
# Add fig_subure title
fig_fin_Expen.update_layout(
    title_text="Apprvd Fin. Support for Teachers(Elementary/Secondary Schools)by Samagra Shiksha(2021-22)",
     autosize=False,
    width=1000,
    height=350,
    xaxis=go.layout.XAxis(linecolor="black", linewidth=1, mirror=True),
    yaxis=go.layout.YAxis(linecolor="black", linewidth=1, mirror=True),
    margin=go.layout.Margin(l=50, r=50, b=100, t=100, pad=4),
)
st.plotly_chart(fig_fin_Expen)