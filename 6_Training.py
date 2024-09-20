import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title='Training',page_icon="📖",
)
st.header('Data About Teacher Training')
st.subheader('Apply Filters')


df_train = pd.read_csv(f'training/Programme-wise Number of Elementary, Secondary and Pre-primary Teachers Trained so far under NISHTHA Training Programme (in reply to Unstarred Question on 15 March, 2023).csv')
df_train .drop(['Sl. No.'], axis=1,inplace=True)

fig_df_train  = go.Figure(data=[go.Table(
    header=dict(values=list(df_train.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=14, color="black"),
                align='left'),
    cells=dict(values=df_train.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=14, color="black"),
               align='left'))
])
# Add fig_subure title
fig_df_train.update_layout(
    title_text="Programme-wise Number of Elementary, Secondary and Pre-primary Teachers Trained so far under NISHTHA Training Programme"
)

st.plotly_chart(fig_df_train)



df_train_inst = pd.read_csv(f'training/StateUTs-wise Number of Teacher Education Institutions recognized by NCTE as on 31.3.2021.csv')
df_train_inst.drop(['Sl. No.'], axis=1,inplace=True)
import plotly.express as px

fig_df_train_inst = px.bar(df_train_inst[df_train_inst['State/UT']!='Total'], x='State/UT', y='No. of Institutions',title='Number of Teacher Education Institutions',height=1000,width=500, text_auto='.2s')

 
st.plotly_chart(fig_df_train_inst)



df_exam = pd.read_csv(f'training/Month Year-wise Passing Percentage of Central Teacher Eligibility Test (CTET) Result form Dec-2018 to Jan-2021.csv')
fig_df_exam  = go.Figure(data=[go.Table(
    header=dict(values=list(df_exam.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=14, color="black"),
                align='left'),
    cells=dict(values=df_exam.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=14, color="black"),
               align='left'))
])
# Add fig_subure title
fig_df_exam .update_layout(
    title_text="Month Year-wise Passing Percentage of Central Teacher Eligibility Test (CTET) Result form Dec-2018"
)


st.plotly_chart(fig_df_exam)

df_perct = pd.read_csv(f'training/StateUT-wise Percentage of Trained Teachers All Types of Management by Gender and Level of School Education during 2021-22 - cleaned.csv')

import plotly.figure_factory as ff
st.subheader(":point_right: StateUT-wise Percentage of Trained Teachers")
with st.expander("Summary_Table- Pre Primary"):

    df_sample=df_perct[['India/State/ UT', 'Pre-Primary - Male', 'Pre-Primary - Female',
       'Pre-Primary - Total']]
    data1=pd.melt(df_sample, id_vars=['India/State/ UT'], value_vars=['Pre-Primary - Male', 'Pre-Primary - Female',
       'Pre-Primary - Total'], var_name='Category',value_name='Percentage')
    data1 = pd.pivot_table(data = data1, values = "Percentage", index = ['India/State/ UT'],columns = "Category")
    # fig = ff.create_table(df_sample, colorscale = "blues")
    # st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("Month wise sub-Category Table")
    #filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
    # sub_category_Year = pd.pivot_table(data = data1, values = "Sales", index = ["Sub-Category"],columns = "month")
    st.write(data1.style.background_gradient(cmap="Blues"))


#st.subheader(":point_right: StateUT-wise Percentage of Trained Teachers")
with st.expander("Summary_Table_Primary"):

    df_sample1=df_perct[['India/State/ UT', 'Primary (1 to 5) - Male',
       'Primary (1 to 5) - Female', 'Primary (1 to 5) - Total']]
    data2=pd.melt(df_sample1, id_vars=['India/State/ UT'], value_vars=['Primary (1 to 5) - Male',
       'Primary (1 to 5) - Female', 'Primary (1 to 5) - Total'], var_name='Category',value_name='Percentage')
    data2 = pd.pivot_table(data = data2, values = "Percentage", index = ['India/State/ UT'],columns = "Category")
    # fig = ff.create_table(df_sample, colorscale = "blues")
    # st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("Month wise sub-Category Table")
    #filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
    # sub_category_Year = pd.pivot_table(data = data1, values = "Sales", index = ["Sub-Category"],columns = "month")
    st.write(data2.style.background_gradient(cmap="Blues"))


#st.subheader(":point_right: StateUT-wise Percentage of Trained Teachers")
with st.expander("Summary_Table_Upper Primary"):

    df_sample2=df_perct[['India/State/ UT', 'Upper Primary (6-8) - Male', 'Upper Primary (6-8) - Female',
       'Upper Primary (6-8) - Total']]
    data3=pd.melt(df_sample2, id_vars=['India/State/ UT'], value_vars=['Upper Primary (6-8) - Male', 'Upper Primary (6-8) - Female',
       'Upper Primary (6-8) - Total'], var_name='Category',value_name='Percentage')
    data3 = pd.pivot_table(data = data3, values = "Percentage", index = ['India/State/ UT'],columns = "Category")
    # fig = ff.create_table(df_sample, colorscale = "blues")
    # st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("Month wise sub-Category Table")
    #filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
    # sub_category_Year = pd.pivot_table(data = data1, values = "Sales", index = ["Sub-Category"],columns = "month")
    st.write(data3.style.background_gradient(cmap="Blues"))


#st.subheader(":point_right: StateUT-wise Percentage of Trained Teachers")
with st.expander("Summary_Table_Secondary"):

    df_sample3=df_perct[['India/State/ UT', 'Secondary (9-10) - Male',
       'Secondary (9-10) - Female', 'Secondary (9-10) - Total'
       ]]
    data4=pd.melt(df_sample3, id_vars=['India/State/ UT'], value_vars=['Secondary (9-10) - Male',
       'Secondary (9-10) - Female', 'Secondary (9-10) - Total'
       ], var_name='Category',value_name='Percentage')
    data4 = pd.pivot_table(data = data4, values = "Percentage", index = ['India/State/ UT'],columns = "Category")
    # fig = ff.create_table(df_sample, colorscale = "blues")
    # st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("Month wise sub-Category Table")
    #filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
    # sub_category_Year = pd.pivot_table(data = data1, values = "Sales", index = ["Sub-Category"],columns = "month")
    st.write(data4.style.background_gradient(cmap="Blues"))

#st.subheader(":point_right: StateUT-wise Percentage of Trained Teachers")
with st.expander("Summary_Table_Higher Secondary"):

    df_sample4=df_perct[['India/State/ UT','Higher Secondary (11-12) - Male', 'Higher Secondary (11-12) - Female',
       'Higher Secondary (11-12) - Total'
       ]]
    data5=pd.melt(df_sample4, id_vars=['India/State/ UT'], value_vars=['Higher Secondary (11-12) - Male','Higher Secondary (11-12) - Female',
       'Higher Secondary (11-12) - Total'
       ], var_name='Category',value_name='Percentage')
    data5 = pd.pivot_table(data = data5, values = "Percentage", index = ['India/State/ UT'],columns = "Category")
    # fig = ff.create_table(df_sample, colorscale = "blues")
    # st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("Month wise sub-Category Table")
    #filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
    # sub_category_Year = pd.pivot_table(data = data1, values = "Sales", index = ["Sub-Category"],columns = "month")
    st.write(data5.style.background_gradient(cmap="Blues"))