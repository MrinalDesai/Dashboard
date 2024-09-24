import os
import pandas as pd
# from dotenv import load_dotenv
import streamlit as st
from snowflake import connector
from snowflake.snowpark import Session
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


myList = list(range(5, 26))

st.set_page_config(page_title='Predicting Teacher Shortage',page_icon="👨🏻‍🏫👩🏻‍🎓")
st.header('Predicting Teacher Shortage')
st.subheader('Lets see how many Teachers we will need to achieve our desired Pupil Teacher Ratio')
st.write('''We have created a synthetic dataset using 
         Data gov and India Economic Monitor Dataset from Marketplace.
         Assuming Indian Population grows at a modest rate of 0.676 percent and our teacher /pupil ratio
         remains steady at around 21.36 pecent we will use simple Math to Predict Teacher Shortage.
         Also Teacher Manpower is assumed to grow at a rate of 2%
         
         ''')

st.subheader('Select a Desired Teacher to Student Ratio from the drop down')

df=pd.read_csv(f'machinelearning/Synthetic_Data.csv')

default_ix = myList.index(25)
ratio_sel=st.selectbox('Select the Option:',myList,placeholder="Select a Desired Pupil to Teacher Ratio",index=default_ix)
df['Shortage']=df['No of Teachers Govt']*(df['pupil_teacher ratio']/ratio_sel/df['growth rate'])-df['No of Teachers Govt']
max_shortage_by_2040=df['Shortage'][df['year']==2040]
#st.write(max_shortage_by_2040.iloc[0])
fig = go.Figure(go.Indicator(
    mode = "number",
    value = ratio_sel,
    number = {'prefix': " Desired Ratio: ","font":{"size":18}},
    
    domain = {'x': [0, 1], 'y': [0, 1]})
               )


    
fig.update_layout(paper_bgcolor = "#0E1117",width=200,height=100)
st.plotly_chart(fig)
##############################################
fig_shor = go.Figure(go.Indicator(
    mode = "number",
    value = max_shortage_by_2040.iloc[0],
    number = {'prefix': " Shortage by 2040: ","font":{"size":22}},
    
    domain = {'x': [0, 1], 'y': [0, 1]})
               )


    
fig_shor.update_layout(paper_bgcolor = "#0E1117",width=500,height=50)
st.plotly_chart(fig_shor)


##############################################
color_list=["aggrnyl", "agsunset", "blackbody", "bluered", "blues", "blugrn", "bluyl", "brwnyl", "bugn", "bupu","burg", "burgyl", "cividis", "darkmint", "electric", "emrld", "gnbu", "greens", "greys", "hot", "inferno","jet", "magenta", "magma", "mint", "orrd", "oranges", "oryel", "peach", "pinkyl", "plasma", "plotly3","pubu", "pubugn", "purd", "purp", "purples", "purpor", "rainbow", "rdbu", "rdpu", "redor", "reds","sunset", "sunsetdark", "teal", "tealgrn", "turbo", "viridis", "ylgn", "ylgnbu", "ylorbr", "ylorrd","algae", "amp", "deep", "dense", "gray", "haline", "ice", "matter", "solar", "speed", "tempo", "thermal","turbid", "armyrose", "brbg", "earth", "fall", "geyser", "prgn", "piyg", "picnic", "portland", "puor","rdgy", "rdylbu", "rdylgn", "spectral", "tealrose", "temps", "tropic", "balance", "curl", "delta", "oxy", "edge", "hsv", "icefire", "phase", "twilight", "mrybm", "mygbm"]


fig = px.bar(df, x='year', y='Shortage',height=500,color='year',color_continuous_scale=color_list[ratio_sel])
st.plotly_chart(fig)

st.write("Scroll to see the data below")

df=df[["year","Shortage","No of Teachers Govt","Population"]]
st.write(df.style.background_gradient(cmap="Blues"))




st.subheader('Conclusion')
st.write('''This looks like a no win situation. So Govt Might lag behind its target.
         
         ''')