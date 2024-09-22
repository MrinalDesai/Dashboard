import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="Internet landscape",
                   page_icon="🌍",
                   )


st.header('Trends In Internet Landscape')
st.write("""Online Learning is the best way to compensate for the high Pupil Teacher Ratio
         Internet connectivity in India is on the rise. With govenment recognising its importance and also 
         private Players playing an Active part the feasability of Online Platforms becomes even more viable.
         BSNL/MTNL lags Behind the private Players but active Goventment Funding can reduce the Gap.
         Wireless Broadband Connections enable Mobility for Students and Ensure more accessibility 
         of Education to Population.
         
         """)

st.write("""
         Internet speeds are vital KPI for providing online education so that Classes can be streamed across wide variety of users
         .The Internet connectivity has steadily Improved in India.Below we have Internet Speed Data of Internet Service Providers""")
st.write("""Below is the Internet Speed Data which shows a upward trend over the years 
         BSNL however lags Behind the private Players.
         
         """)
st.subheader("#️⃣India Telecom Data About Internet Speed 2018-2023-MySpeed📌 ", divider="gray")
st.write("""""")

st.subheader('Apply Filters')


df_speed = pd.read_csv(f'internet/India Telecom Data About Internet Speed 2018-2023-MySpeed.csv')
df_speed['Year']=df_speed['Year'].astype('category')

# --- STREAMLIT SELECTION
service_provider = df_speed['Service Provider'].unique().tolist()
circle = df_speed['Circle'].unique().tolist()




circle_selection=st.multiselect('States:',
                                    circle,
                                    default='INDIA')



if not circle_selection:
    circle_selection=['INDIA']

# --- FILTER DATAFRAME BASED ON SELECTION
mask_speed = (df_speed['Circle'].isin(circle_selection)) #(df_speed['Service Provider'].isin(service_provider_selection))&\




# --- GROUP DATAFRAME AFTER SELECTION.grou
df_speed_grouped = df_speed[mask_speed].groupby(['Service Provider','Year'],as_index=False)[['Data Speed(Mbps)']].mean()
df_speed_grouped['Data Speed(Mbps)']=df_speed_grouped['Data Speed(Mbps)'].astype(int)

df_speed_grouped = df_speed_grouped.reset_index()



fig_speed = px.bar(df_speed_grouped, x="Service Provider", y="Data Speed(Mbps)", 
             color="Year", text='Data Speed(Mbps)',barmode = 'group')

st.plotly_chart(fig_speed)

st.subheader("#️⃣India Telecom Data About Data Usage and per GB Tariff📌 ", divider="gray")
st.write("""As we see below the Data Usage as well Subscribers acoross country have steadily Increased""")

df_tariff = pd.read_csv(f'internet/Quarter wise Wireless Data Usage and per GB Tariff Qtr1 2017-18 to Qtr3 2022-23.csv')



import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig_usage = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig_usage.add_trace(
    go.Scatter(x=df_tariff['Duration'], y=df_tariff['Total Quarterly Usage - Current (PB)'], name='Total Quarterly Usage - Current (PB)'),
    secondary_y=False,
)

fig_usage.add_trace(
    go.Scatter(x=df_tariff['Duration'], y=df_tariff['Per Subscriber per Month - Current (MB)'], name="Per Subscriber per Month - Current (MB)"),
    secondary_y=True,
)

# Add figure title
fig_usage.update_layout(
    title_text="Internet/Quarter wise Wireless Data Usage Qtr1 2017-18 to Qtr3 2022-23"
)

# Set x-axis title
fig_usage.update_xaxes(title_text="Duration Quarterly 2007-2023")

# Set y-axes titles
fig_usage.update_yaxes(title_text="<b>Tot Qtr Usage</b> (PB)", secondary_y=False)
fig_usage.update_yaxes(title_text="<b>Per Subs. per Mnt.</b> (MB)", secondary_y=True)

st.plotly_chart(fig_usage)


# Create figure with secondary y-axis
fig_tariff = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig_tariff .add_trace(
    go.Scatter(x=df_tariff['Duration'], y=df_tariff['Tariff per GB - Current (Rs.)'], name='Tariff per GB - Current (Rs.)'),
    secondary_y=False,
)



# Add figure title
fig_tariff .update_layout(
    title_text="Internet/Quarter wise Wireless Data Tariff Qtr1 2017-18 to Qtr3 2022-23"
)

# Set x-axis title
fig_tariff .update_xaxes(title_text="Duration Quarterly 2017-2023")

# Set y-axes titles
fig_tariff .update_yaxes(title_text="<b>Tariff per GB </b>(Rs.)", secondary_y=False)
fig_tariff .update_layout(showlegend=True)

st.write("""Another Positive trend we see is the Decreasing Tariff which makes it more Affordable for the masses
         Wireless Technology enables users to access Classes while on the Go and overcomes location criteria""")

st.plotly_chart(fig_tariff)




df_mtnl = pd.read_csv(f'internet/MTNL_Performance-April2014-May2023.csv')

# Create fig_mtnl_custure with secondary y-axis
fig_mtnl_cust = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig_mtnl_cust.add_trace(
    go.Scatter(x=df_mtnl['Duration'], y=df_mtnl['Wireless Customers - Cumulative (Lakhs)'], name='Wireless Customers - Cumulative (Lakhs)'),
    secondary_y=False,
)

fig_mtnl_cust.add_trace(
    go.Scatter(x=df_mtnl['Duration'], y=df_mtnl['Wireline Customers - Cumulative (Lakhs)'], name='Wireline Customers - Cumulative (Lakhs)'),
    secondary_y=True,
)

# Add fig_mtnl_custure title
fig_mtnl_cust.update_layout(
    title_text="MTNL Performance April2014-May2023"
)

# Set x-axis title
fig_mtnl_cust.update_xaxes(title_text="Duration Month")

# Set y-axes titles
fig_mtnl_cust.update_yaxes(title_text="<b>Wireless Cust </b>(Lakhs)", secondary_y=False)
fig_mtnl_cust.update_yaxes(title_text="<b>Wireline Cust </b> (Lakhs)", secondary_y=True)

st.plotly_chart(fig_mtnl_cust)


# Create fig_mtnl_usageure with secondary y-axis
fig_mtnl_usage = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig_mtnl_usage.add_trace(
    go.Scatter(x=df_mtnl['Duration'], y=df_mtnl['Data Consumption - Cumulative (TB)'], name='Data Consumption - Cumulative (TB)'),
    secondary_y=False,
)

fig_mtnl_usage.add_trace(
    go.Scatter(x=df_mtnl['Duration'], y=df_mtnl['No. of Digital Payments (Lakhs)'], name='No. of Digital Payments (Lakhs)'),
    secondary_y=True,
)

# Add fig_mtnl_usageure title
fig_mtnl_usage.update_layout(
    title_text="MTNL Performance April2014-May2023"
)

# Set x-axis title
fig_mtnl_usage.update_xaxes(title_text="Duration Month")

# Set y-axes titles
fig_mtnl_usage.update_yaxes(title_text="<b>'Data Consumption' </b>(TB)", secondary_y=False)
fig_mtnl_usage.update_yaxes(title_text="<b>'No. Digital Payments'</b>(Lakhs)", secondary_y=True)

st.subheader("#️⃣MTNL📌 ", divider="gray")
st.write("""Government Players however have not performed well and need to catch up""")

st.plotly_chart(fig_mtnl_usage)


st.subheader("#️⃣Teledensity📌 ", divider="gray")
st.write("""Government needs to Improve Teledensity in Rural Sectors. Urbanisation of Rural areas will reduce this problem""")

df_pene = pd.read_csv(f'internet/StateUT-wise Details of Internet Penetration (Internet Subscribers per 100 Population) in UrbanRural Areas of the Country as on 31st March 2024.csv')
df_pene['State/UT']=df_pene['State/UT'].replace('Total', 'INDIA')
state = df_pene['State/UT'].unique().tolist()

state_selection=st.multiselect('States:',
                                    state,
                                    default='INDIA')

if not state_selection:
    state_selection=['INDIA']


# --- FILTER DATAFRAME BASED ON SELECTION
mask_pen = (df_pene['State/UT'].isin(state_selection)) 

# Select numeric columns.
a = df_pene.select_dtypes('number')
# Select string and object columns.
b = df_pene.select_dtypes('object')

# Fill numeric columns with mean.
df_pene[a.columns] = a.fillna(a.mean())



df_pene_unpivot_sub = pd.melt(df_pene[mask_pen], id_vars=['State/UT'], value_vars=[ 'Total Subscribers (In Million) - Rural',
       'Total Subscribers (In Million) - Urban',
       'Total Subscribers (In Million) - Total'],var_name='Subscribers (In Million)', value_name='No of Sub (In Million)')



df_pene_unpivot_telden = pd.melt(df_pene[mask_pen], id_vars=['State/UT'], value_vars=[ 'Teledensity (%) - Rural',
       'Teledensity (%) - Urban', 'Teledensity (%) - Total'],var_name='Teledensity Urban/Rural/Total(%)', value_name='Teledensity (%)')






# --- GROUP DATAFRAME AFTER SELECTION.grou
df_grouped_no_sub = df_pene_unpivot_sub.groupby(['Subscribers (In Million)'],as_index=False)[['No of Sub (In Million)']].mean()
#df_grouped_no_sub['No of Sub (In Million)']=df_grouped_no_sub['No of Sub (In Million)'].astype(int)
df_grouped_no_sub['No of Sub (In Million)']=df_grouped_no_sub['No of Sub (In Million)'].round(decimals=2)
#df_grouped = df_grouped.rename(columns={'Age': 'Votes'})
df_grouped_no_sub = df_grouped_no_sub.reset_index(drop=True)

# --- GROUP DATAFRAME AFTER SELECTION.grou
df_grouped_telden = df_pene_unpivot_telden.groupby(['Teledensity Urban/Rural/Total(%)'],as_index=False)[['Teledensity (%)']].mean()
#df_grouped_telden['Teledensity (%)']=df_grouped_telden['Teledensity (%)'].astype(int)
df_grouped_telden['Teledensity (%)']=df_grouped_telden['Teledensity (%)'].round(decimals=2)
#df_grouped = df_grouped.rename(columns={'Age': 'Votes'})
df_grouped_telden = df_grouped_telden.reset_index(drop=True)


fig_telden = px.bar(df_grouped_telden, x="Teledensity Urban/Rural/Total(%)", y="Teledensity (%)", 
             color="Teledensity Urban/Rural/Total(%)", text="Teledensity (%)",barmode = 'group')


 


fig_no_sub = px.bar(df_grouped_no_sub, x="Subscribers (In Million)", y="No of Sub (In Million)", 
             color="No of Sub (In Million)", text="No of Sub (In Million)",barmode = 'group')



st.plotly_chart(fig_telden)

st.plotly_chart(fig_no_sub)



df_sub_ur = pd.read_csv(f'internet/Month-wise_InternetSubscribers-Rural_vs_Urban-Broadband_vs_Narrowband-April_2014-to-Dec_2022.csv')

# Create fig_subure with secondary y-axis
fig_sub = make_subplots(specs=[[{"secondary_y": False}]])

# Add traces
fig_sub.add_trace(
    go.Scatter(x=df_sub_ur['Duration'], y=df_sub_ur['Total Subscribers - Cumulative (Crore)'], name='Total Subscribers - Cumulative (Crore)'),
    secondary_y=False,
)

fig_sub.add_trace(
    go.Scatter(x=df_sub_ur['Duration'], y=df_sub_ur['Broadband Subscribers - Cumulative (Crore)'], name='Broadband Subscribers - Cumulative (Crore)'),
    secondary_y=False,
)

fig_sub.add_trace(
    go.Scatter(x=df_sub_ur['Duration'], y=df_sub_ur['Narrowband Subscribers - Cumulative (Crore)'], name='Narrowband Subscribers - Cumulative (Crore)'),
    secondary_y=False,
)

fig_sub.add_trace(
    go.Scatter(x=df_sub_ur['Duration'], y=df_sub_ur['Urban Subscribers - Cumulative (Crore)'], name='Urban Subscribers - Cumulative (Crore)'),
    secondary_y=False,
)

fig_sub.add_trace(
    go.Scatter(x=df_sub_ur['Duration'], y=df_sub_ur['Rural Subscribers - Cumulative (Crore)'], name='Rural Subscribers - Cumulative (Crore)'),
    secondary_y=False,
)
# Add fig_subure title
fig_sub.update_layout(
    title_text="Month-wise Internet Subscribers-Rural vs Urban-Broadband vs Narrowband April 2014-to-Dec 2022"
)

# Set x-axis title
fig_sub.update_xaxes(title_text="Duration Month April_2014-to-Dec_2022")

# Set y-axes titles
fig_sub.update_yaxes(title_text="<b>Subscribers </b>(Crore)", secondary_y=False)

st.subheader("#️⃣Type of Connections📌 ", divider="gray")
st.write("""Among the Technologies Broadband connections are on the rise but here also the Rural sector lags behind.""")

st.plotly_chart(fig_sub)

df_sub_wi = pd.read_csv(f'internet/Month-wise Broadband Subscribers Wireline vs Wireless April 2014 to Dec_2022.csv')

# Create fig_wrure with secondary y-axis
fig_wr = make_subplots(specs=[[{"secondary_y": False}]])

# Add traces
fig_wr.add_trace(
    go.Scatter(x=df_sub_wi['Duration'], y=df_sub_wi['Total Subscribers - Cumulative (Crore)'], name='Total Subscribers - Cumulative (Crore)'),
    secondary_y=False,
)

fig_wr.add_trace(
    go.Scatter(x=df_sub_wi['Duration'], y=df_sub_wi['Wireless Subscribers - Cumulative (Crore)'], name='Wireless Subscribers - Cumulative (Crore)'),
    secondary_y=False,
)

fig_wr.add_trace(
    go.Scatter(x=df_sub_wi['Duration'], y=df_sub_wi['Wireline Subscribers - Cumulative (Crore)'], name='Wireline Subscribers - Cumulative (Crore)'),
    secondary_y=False,
)


# Add fig_wrure title
fig_wr.update_layout(
    title_text="Month-wise Broadband Subscribers Wireline vs Wireless Apr 2014-Dec 2022"
)

# Set x-axis title
fig_wr.update_xaxes(title_text="Duration Month April_2014-to-Dec_2022")

# Set y-axes titles
fig_wr.update_yaxes(title_text="<b>Subscribers </b>(Crore)", secondary_y=False)


st.plotly_chart(fig_wr)



import plotly.graph_objects as go
from plotly.subplots import make_subplots
df_bsnl_sub = pd.read_csv(f'internet/table/Subscribers of Bharat Sanchar Nigam Limited (BSNL) from 2016 to 2020 (From Ministry of Communications).csv')
df_bsnl_sub['Number of Subscribers']=round(df_bsnl_sub['Number of Subscribers']/10000000,2)
fig_bsnl_sub = go.Figure(data=[go.Table(
    header=dict(values=list(df_bsnl_sub.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=14, color="black"),
                align='left'),
    cells=dict(values=df_bsnl_sub.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=14, color="black"),
               align='left'))
])
# Add fig_subure title
fig_bsnl_sub.update_layout(
    title_text="Subscribers In Crores of (BSNL)2016-20"
)


st.subheader("#️⃣BSNL📌 ", divider="gray")
st.write("""BSNL subscribers have remained relatively constant over the years.""")

st.plotly_chart(fig_bsnl_sub)


df_bsnl_pl = pd.read_csv(f'internet/table/PSU-wise ProfitLoss of Bharat Sanchar Nigam Limited (BSNL) and Mahanagar Telephone Nigam Limited (MTNL) from 2018-19 to 2020-21.csv')

fig_bsnl_pl = go.Figure(data=[go.Table(
    header=dict(values=list(df_bsnl_pl.columns),
                fill_color='darkturquoise',
                # fill_color='#b9e2ff',
                line_color='darkslategray',
                font = dict(family="Arial", size=14, color="black"),
                align='left'),
    cells=dict(values=df_bsnl_pl.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=14, color="black"),
               align='left'))
])
# Add fig_subure title
fig_bsnl_pl.update_layout(
    title_text="ProfitLoss of (BSNL) and (MTNL) Crores"
)

st.subheader("#️⃣BSNL/MTNL Performance📌 ", divider="gray")
st.write("""BSNL and MTNL has suferred heavy losses over the years.""")
st.plotly_chart(fig_bsnl_pl)

import plotly.graph_objects as go
from plotly.subplots import make_subplots
df_bsnl_funds = pd.read_csv(f'internet/table/Year-wise Details of Funds given to Bharat Sanchar Nigam Limited (BSNL) and Mahanagar Telephone Nigam Limited MTNL from 2019-20 to 2022-23.csv')
fig_bsnl_funds = go.Figure(data=[go.Table(
    header=dict(values=list(df_bsnl_funds.columns),
                fill_color='darkturquoise',
                
                line_color='darkslategray',
                font = dict(family="Arial", size=14, color="black"),
                align='left'),
    cells=dict(values=df_bsnl_funds.transpose().values.tolist(),
               fill_color='lightgray',
                font = dict(family="Arial", size=14, color="black"),
               align='left'))
])
# Add fig_subure title
fig_bsnl_funds.update_layout(
    title_text="ProfitLoss of (BSNL) and (MTNL)"
)

st.subheader("#️⃣Government Funding📌 ", divider="gray")
st.write("""BSNL has recieved good amount of Funding from the Govt.""")
# st.plotly_chart(fig_bsnl_pl)
st.plotly_chart(fig_bsnl_funds)


st.header('Summary')
st.write("""
Above all Satistics Indicate that the trend of Online learning will Continue. With Private players performing well
         and Govt playing an active part Future for online learning remains bright.


""")