import os
import pandas as pd
# from dotenv import load_dotenv
import streamlit as st
from snowflake import connector
from snowflake.snowpark import Session
df_stats = pd.read_csv(f'live_stats/Database.csv')


# Import the necessary module
from dotenv import load_dotenv
import os
load_dotenv()
print(st.secrets["SPASSWORD"])
# PASSWORD = os.getenv('PASSWORD')
# USER1 = os.getenv('USER1')
# ACCOUNT1 = os.getenv('ACCOUNT1')

PASSWORD = st.secrets["SPASSWORD"]
USER2 = st.secrets['SUSER2'] 
ACCOUNT2 = st.secrets['SACCOUNT2'] 
#########################################
st.set_page_config(page_title="Live Data",
                   page_icon="📥",
                   )

st.title("Lets Use\n :red[INDIA SOCIAL IMPACT_DATA SET]💾 to View some Stats :")
st.subheader("#️⃣Lets Fetch some Live stats📈")
st.subheader("🚩👣Steps to Use:")
st.write("""🚩Choose youe Data from the Drop-Down List""")
st.write("""🚩Chick on the Fetch Data Button""")
st.write("""🚩Scroll to View Entire dataset and Save Data by using Download option In the Top Corner""")
#########################################

title = df_stats['TITLE'].unique().tolist()  

title_sel=st.selectbox('Select the Option:',title,placeholder="Select a Option to Display Data")
identifier=df_stats['IDENTIFIER'][df_stats['TITLE']==title_sel].iloc[0]

st.write("Identifier:", identifier)



query='SELECT * from HACKATHON.IDH_DATA WHERE Identifier in ('+"'"+identifier+"'"+');'
st.write("Query:", query)
connection_params = {
    "account": ACCOUNT1,
    "user": USER1,
    "password": PASSWORD,
    "database":"INDIA_SOCIAL_IMPACT_DATA_SET",
    "schema": "HACKATHON"
    # "role":"ACCOUNTADMIN"
}





import snowflake.connector
import pandas as pd

# Gets the version





# query = '''
# SELECT * from HACKATHON.IDH_DATA
# WHERE
#     Identifier in ('SSEDUNIDUA11A') and Date between '2000-03-31' and  '2024-03-31';
# '''




with st.form("Input"):
    # queryText = st.text_area("SQL to execute:", height=3, max_chars=None)
    btnResult = st.form_submit_button('Fetch Data')

if btnResult:
    # Create a Snowflake session
    session = Session.builder.configs(connection_params).create()
    ctx = snowflake.connector.connect(
    user=USER1,
    password=PASSWORD,
    account=ACCOUNT1
    
    )
    
    ctx.cursor().execute('USE INDIA_SOCIAL_IMPACT_DATA_SET.HACKATHON')
    cur = ctx.cursor().execute(query)
    df = pd.DataFrame.from_records(iter(cur), columns=[x[0] for x in cur.description])
    st.write(df.style.background_gradient(cmap="Blues"))
    st.text('Fetched Results')
    
    # run query
    # st.write(queryText)