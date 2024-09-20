import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots


st.set_page_config(page_title="Internet Infrastructure",
                   page_icon="🌍",
                   )
df_CF=pd.read_csv(f'infra/per/by Management and Availability of Computer Facility during 2021-22.csv')
df_CFP=pd.read_csv(f'infra/per/by Management and Availability of Computer Facility during 2021-22_Per.csv')
df_LabsP=pd.read_csv(f'infra/per/Details of Information and Communication Technology (ICT) Labs, Smart Classrooms and Tabs Sanctioned for Teacher Resource Package_no.csv')
df_Laptop=pd.read_csv(f'infra/per/Functional LaptopNotebook Available during 2021-22.csv')
df_Laptop_Per=pd.read_csv(f'infra/per/Functional LaptopNotebook Available during 2021-22_Per.csv')
df_Mobile=pd.read_csv(f'infra/per/Functional Mobile Phones Used for Teaching Purposes during 2021-22.csv')
df_Mobile_Per=pd.read_csv(f'infra/per/Functional Mobile Phones Used for Teaching Purposes during 2021-22_Per.csv')
df_PC=pd.read_csv(f'infra/per/PCs with Functional Integrated Teaching Learning Devices Available during 2021-22.csv')
df_PC_Per=pd.read_csv(f'infra/per/PCs with Functional Integrated Teaching Learning Devices Available during 2021-22_Per.csv')
df_Peer=pd.read_csv(f'infra/per/Peer Learning by Education Level and Management during 2021-22_No.csv')
df_Peer_Per=pd.read_csv(f'infra/per/Peer Learning by Education Level and Management during 2021-22_Per.csv')


lst=df_CF.columns.to_list()
lst.remove('State/UT')
lst.remove('Category')
df_CF=pd.melt(df_CF, id_vars=['State/UT','Category'], value_vars=lst, var_name='Column_Names',value_name='Number/Percentage')

lst=df_CFP.columns.to_list()
lst.remove('State/UT')
lst.remove('Category')
df_CFP=pd.melt(df_CFP, id_vars=['State/UT','Category'], value_vars=lst, var_name='Column_Names',value_name='Number/Percentage')

lst=df_LabsP.columns.to_list()
lst.remove('State/UT')
lst.remove('Category')
df_LabsP=pd.melt(df_LabsP, id_vars=['State/UT','Category'], value_vars=lst, var_name='Column_Names',value_name='Number/Percentage')

lst=df_Laptop.columns.to_list()
lst.remove('State/UT')
lst.remove('Category')
df_Laptop=pd.melt(df_Laptop, id_vars=['State/UT','Category'], value_vars=lst, var_name='Column_Names',value_name='Number/Percentage')

lst=df_Laptop_Per.columns.to_list()
lst.remove('State/UT')
lst.remove('Category')
df_Laptop_Per=pd.melt(df_Laptop_Per, id_vars=['State/UT','Category'], value_vars=lst, var_name='Column_Names',value_name='Number/Percentage')


lst=df_Mobile.columns.to_list()
lst.remove('State/UT')
lst.remove('Category')
df_Mobile=pd.melt(df_Mobile, id_vars=['State/UT','Category'], value_vars=lst, var_name='Column_Names',value_name='Number/Percentage')

lst=df_Mobile_Per.columns.to_list()
lst.remove('State/UT')
lst.remove('Category')
df_Mobile_Per=pd.melt(df_Mobile_Per, id_vars=['State/UT','Category'], value_vars=lst, var_name='Column_Names',value_name='Number/Percentage')

lst=df_PC.columns.to_list()
lst.remove('State/UT')
lst.remove('Category')
df_PC=pd.melt(df_PC, id_vars=['State/UT','Category'], value_vars=lst, var_name='Column_Names',value_name='Number/Percentage')


lst=df_PC_Per.columns.to_list()
lst.remove('State/UT')
lst.remove('Category')
df_PC_Per=pd.melt(df_PC_Per, id_vars=['State/UT','Category'], value_vars=lst, var_name='Column_Names',value_name='Number/Percentage')

lst=df_Peer.columns.to_list()
lst.remove('State/UT')
lst.remove('Category')
df_Peer=pd.melt(df_Peer, id_vars=['State/UT','Category'], value_vars=lst, var_name='Column_Names',value_name='Number/Percentage')


lst=df_Peer_Per.columns.to_list()
lst.remove('State/UT')
lst.remove('Category')
df_Peer_Per=pd.melt(df_Peer_Per, id_vars=['State/UT','Category'], value_vars=lst, var_name='Column_Names',value_name='Number/Percentage')


df_infra=pd.concat([df_CF,
df_CFP,
df_LabsP,
df_Laptop,
df_Laptop_Per,
df_Mobile,
df_Mobile_Per,
df_PC,
df_PC_Per,
df_Peer,
df_Peer_Per] ,ignore_index = True)

cat = df_infra['Category'].unique().tolist()  

cat_sel=st.selectbox('Category:',cat,placeholder="Select a Option to Display Data")


mask_cat = (df_infra['Category']==cat_sel) 

df_filtered = df_infra[mask_cat]
df_filtered_ind = df_filtered[df_filtered['State/UT']=="INDIA"]
df_filtered = df_filtered[df_filtered['State/UT']!="INDIA"]

#st.subheader(":point_right: StateUT-wise Percentage of Trained Teachers")
with st.expander("Statewise Data"):
    final_table=pd.pivot_table(data = df_filtered, values = "Number/Percentage", index = ['State/UT'],columns = "Column_Names")
    st.markdown("Month wise sub-Category Table")
    #filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
    # sub_category_Year = pd.pivot_table(data = data1, values = "Sales", index = ["Sub-Category"],columns = "month")
    st.write(final_table.style.background_gradient(cmap="Blues"))



# with st.expander("India Data"):
temp1=df_filtered_ind.drop('Category', axis=1).reset_index()

temp1=temp1[['Column_Names','Number/Percentage']]
temp1=temp1.rename({'Column_Names': 'Type'}, axis=1)
st.markdown(df_filtered_ind['Category'].iloc[0])
#filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
# sub_category_Year = pd.pivot_table(data = data1, values = "Sales", index = ["Sub-Category"],columns = "month")
st.write(temp1.style.background_gradient(cmap="Blues"))