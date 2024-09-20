import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go

st.set_page_config(page_title='👩🏻‍🏫Teaching landscape',page_icon="👩🏻‍🏫",)
st.header('Data About Teachers')
st.subheader('Apply Filters')

df_nos_state= pd.read_csv(f'nos/StateUT-wise Number of Teachers-Categories.csv')
#df_nos_state=df_nos[(df_nos['Category']=='All Types of Management and School Category') & (df_nos['Sub-Category']=='Number of Teachers - All Types of Management - Total')]

# --- STREAMLIT SELECTION

cat = df_nos_state['Category'].unique().tolist()  
sub_cat= df_nos_state['Sub-Category'].unique().tolist()


cat_sel=st.selectbox('Category:',cat,placeholder="Select a Option to Display Data")

sub_cat= df_nos_state[df_nos_state['Category']==cat_sel]['Sub-Category'].unique().tolist()

sub_cat_sel= st.selectbox('Sub_Category:',sub_cat,placeholder="Select a Option to Display Data")



# if not cat_sel:
#     cat_sel=['Number of Teachers - All Types of Management - Total']
    
# if not sub_cat_sel:
#     cat_sel=['Number of Teachers - All Types of Management - Total']
#     sub_cat_sel=['All Types of Management and School Category']
#     if not cat_sel:
#        cat_sel=['Number of Teachers - All Types of Management - Total']
    
# --- FILTER DATAFRAME BASED ON SELECTION
mask_cat = (df_nos_state['Category']==cat_sel) & (df_nos_state['Sub-Category']==sub_cat_sel) & (df_nos_state['India/State /UT']!='India')
mask_cat_India = (df_nos_state['Category']==cat_sel) & (df_nos_state['Sub-Category']==sub_cat_sel)&(df_nos_state['India/State /UT']=='India')
# --- GROUP DATAFRAME AFTER SELECTION.grou
df_grouped = df_nos_state[mask_cat].groupby('India/State /UT',as_index=False)[['Value']].mean()
df_grouped['Value']=df_grouped['Value'].astype(int)
#df_grouped = df_grouped.rename(columns={'Age': 'Votes'})
df_grouped = df_grouped.reset_index()


# --- GROUP DATAFRAME AFTER SELECTION.grou
df_grouped_ind = df_nos_state[mask_cat_India].groupby('India/State /UT',as_index=False)[['Value']].sum()
df_grouped_ind['Value']=df_grouped_ind['Value'].astype(int)
#df_grouped = df_grouped.rename(columns={'Age': 'Votes'})
df_grouped_ind = df_grouped_ind.reset_index()

if not sub_cat:
    sub_cat=['Number of Teachers - All Types of Management - Total']

if not cat:
    cat=['All Types of Management and School Category']

fig = go.Figure(go.Indicator(
    mode = "number",
    value = df_grouped_ind['Value'].mean(),
    number = {'prefix': "India: ","font":{"size":25}},
    
    domain = {'x': [0, 1], 'y': [0, 1]})
               )
    
fig.update_layout(paper_bgcolor = "#0E1117",width=200,height=100)
st.plotly_chart(fig)
# st.plotly_chart(fig)
fig1 = px.bar(df_grouped, x='India/State /UT', y='Value',title="Teachers Distribution Statewise",labels={'Value':'Total no of Teachers'})

st.plotly_chart(fig1)



df_nos_cu= pd.read_csv(f'nos/Cen_Uni_Data.csv')

import plotly.graph_objects as go
from plotly.subplots import make_subplots

df_nos_cu = pd.read_csv(f'nos/Cen_Uni_Data.csv')
fig_nos_cu = go.Figure(data=[go.Table(
    header=dict(values=list(df_nos_cu.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=12, color="black"),
                align='left'),
    cells=dict(values=df_nos_cu.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=10, color="black"),
               align='left'))
])
# Add fig_subure title
fig_nos_cu.update_layout(
    title_text="Central Universities posts details"
)
st.plotly_chart(fig_nos_cu)

#################################################


df_nos_va= pd.read_csv(f'nos/StateUTs-wise Detail of Vacancy of Teachers in Government Schools from 2019-20 to 2021-22_No.csv')
df_per_va= pd.read_csv(f'nos/StateUTs-wise Detail of Vacancy of Teachers in Government Schools from 2019-20 to 2021-22_Per.csv')

state_va= df_nos_va['State/UTs'].unique().tolist() 




va_sel=st.selectbox('State/UTs:',state_va,placeholder="Select a Option to Display Data",index=36)


# --- FILTER DATAFRAME BASED ON SELECTION
mask_va = (df_nos_va['State/UTs']==va_sel) 



df_nos_va=df_nos_va[mask_va]
df_per_va=df_per_va[mask_va]


df_va_no = df_nos_va
fig_va_no = go.Figure(data=[go.Table(
    header=dict(values=list(df_va_no.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=14, color="black"),
                align='left'),
    cells=dict(values=df_va_no.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=14, color="black"),
               align='left'))
])
# Add fig_subure title
fig_va_no.update_layout(
    title_text="StateUTs-wise Detail of Vacancy of Teachers in Government Schools Nos"
)



df_per_no = df_per_va
fig_va_pe = go.Figure(data=[go.Table(
    header=dict(values=list(df_per_no.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=14, color="black"),
                align='left'),
    cells=dict(values=df_per_no.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=14, color="black"),
               align='left'))
])
# Add fig_subure title
fig_va_pe.update_layout(
    title_text="StateUTs-wise Detail of Vacancy of Teachers in Government Schools Percentage"
)

st.plotly_chart(fig_va_no)
st.plotly_chart(fig_va_pe)


df_single= pd.read_csv(f'nos/StateUT-wise Number of Single Teacher Schools 2017-22.csv')
state_single= df_single['State/UTs'].unique().tolist()  
va_single=st.selectbox('State/UTs:',state_single,placeholder="Select a Option to Display Data",index=35)
# # --- FILTER DATAFRAME BASED ON SELECTION
mask_single = (df_single['State/UTs']==va_single)
df_single=df_single[mask_single]

fig_single = go.Figure(data=[go.Table(
    header=dict(values=list(df_single.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=14, color="black"),
                align='left'),
    cells=dict(values=df_single.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=14, color="black"),
               align='left'))
])
# Add fig_subure title
fig_single.update_layout(
    title_text="StateUTs-wise Single Teacher Schools"
)


st.plotly_chart(fig_single)
