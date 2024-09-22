import os
import pandas as pd
# from dotenv import load_dotenv
import streamlit as st
from snowflake import connector
from snowflake.snowpark import Session
import numpy as np
import plotly.express as px

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



st.write(df.style.background_gradient(cmap="Blues"))

fig = px.bar(df, x='year', y='Shortage')
st.plotly_chart(fig)


st.subheader('Conclusion')
st.write('''This looks like a no win situation. So Govt Might lag behind its target.
         
         ''')