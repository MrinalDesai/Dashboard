import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='👨🏻‍🏫Teacher to 👩🏻‍🎓Pupil Ratio',page_icon="👨🏻‍🏫👩🏻‍🎓")
st.header('Student Pupil Ratio States Yearwise')
st.subheader('Apply Filters')
st.write('''In this section we have explored Teacher to Student Ratio of India as well 
         as individual States. Though the numbers are improving with Population growth
         and Resource Allocation we Cannot cconsider this as a good Situation''')

### --- LOAD DATAFRAME
df = pd.read_csv('State UT and School-wise Pupil teacher ratio (PTR) for 2008-2022.csv')
df[' Primary (1 to 5)'] = df[' Primary (1 to 5)'].fillna(df.groupby('States/Union Territories')[' Primary (1 to 5)'].transform('mean'))
df['Higher Secondary (11-12)'] = df['Higher Secondary (11-12)'].fillna(df.groupby('States/Union Territories')['Higher Secondary (11-12)'].transform('mean'))
df['Secondary (9-10)'] = df['Secondary (9-10)'].fillna(df.groupby('States/Union Territories')['Secondary (9-10)'].transform('mean'))
df['Upper Primary (6-8)'] = df['Upper Primary (6-8)'].fillna(df.groupby('States/Union Territories')['Upper Primary (6-8)'].transform('mean'))

df_unpivot = pd.melt(df, id_vars=['States/Union Territories','Year'], value_vars=['Higher Secondary (11-12)',
       'Secondary (9-10)', 'Upper Primary (6-8)', ' Primary (1 to 5)'],var_name='Education_Level', value_name='Ratio')

# --- STREAMLIT SELECTION
year = df_unpivot['Year'].unique().tolist()
states = df_unpivot['States/Union Territories'].unique().tolist()

level_value=df_unpivot['Education_Level'].unique().tolist()
ratio_value=df_unpivot['Ratio'].unique().tolist()






# year_selection = st.sidebar.multiselect('Year:',
#                                     year,
#                                     default='2021-2022')

st.write("Select Multiple options to Find the Average over the years or accross States")

year_selection = st.multiselect('Year:',
                                    year,
                                    default='2021-2022')

if not year_selection:
    st.write("Select a Year")

# states_selection = st.sidebar.multiselect('States:',
#                                     states,
#                                     default='INDIA')

states_selection = st.multiselect('States:',
                                    states,
                                    default='INDIA')

if not states_selection:
    states_selection=['INDIA']
    



if not year_selection:
    year_selection=['2021-2022']





# --- FILTER DATAFRAME BASED ON SELECTION
mask =(df_unpivot['States/Union Territories'].isin(states_selection))& (df_unpivot['Year'].isin(year_selection))



# --- GROUP DATAFRAME AFTER SELECTION.grou
df_grouped = df_unpivot[mask].groupby('Education_Level',as_index=False)[['Ratio']].mean()
df_grouped['Ratio']=df_grouped['Ratio'].astype(int)
#df_grouped = df_grouped.rename(columns={'Age': 'Votes'})
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped,
                   x='Education_Level',
                   y='Ratio',
                   text='Ratio',
                   color_discrete_sequence = ['#7792E3']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)



states_selection_year = st.multiselect('States Year-Wise:',
                                    states,
                                    default='INDIA')

if not states_selection_year:
    states_selection_year=['INDIA']
# --- FILTER DATAFRAME BASED ON SELECTION
mask_state = (df_unpivot['States/Union Territories'].isin(states_selection_year))

df_grouped_year=df_unpivot[mask_state].groupby(['Education_Level','Year'],as_index=False)[['Ratio']].mean() 
df_grouped_year = df_grouped_year.reset_index()


fig = px.bar(df_grouped_year, x="Education_Level", y="Ratio", 
             color="Year", text='Ratio',barmode = 'group')


st.plotly_chart(fig)
