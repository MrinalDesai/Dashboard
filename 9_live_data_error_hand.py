import os
import pandas as pd
# from dotenv import load_dotenv
import streamlit as st
from snowflake import connector
from snowflake.snowpark import Session
from snowflake.connector.errors import DatabaseError, ProgrammingError
df_stats = pd.read_csv(f'live_stats/Database.csv')


# Import the necessary module
from dotenv import load_dotenv
import os
load_dotenv()

# PASSWORD = os.getenv('PASSWORD')
# USER1 = os.getenv('USER1')
# ACCOUNT1 = os.getenv('ACCOUNT1')

PASSWORD = st.secrets["SPASSWORD"]
USER1 = st.secrets['SUSER1'] 
ACCOUNT1 = st.secrets['SACCOUNT1'] 
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

try:
    con = snowflake.connector.connect(
        user=USER1,       # <-------- Bad user
        password=PASSWORD,   # <-------- Bad pass
        account=ACCOUNT1 , # <-------- This is correct
        database="INDIA_SOCIAL_IMPACT_DATA_SET",
        schema= "HACKATHON"
    )
except DatabaseError as db_ex:
    if db_ex.errno == 250001:
        st.write(f"Invalid username/password, please re-enter username and password...")
        # code for user to re-enter username & pass
    else:
        raise
except Exception as ex:
    # Log this
    st.write(f"Some error you don't know how to handle {ex}")
    raise
else:
    try:
        session = Session.builder.configs(connection_params).create()
        ctx = snowflake.connector.connect(
        user=USER1,
        password=PASSWORD,
        account=ACCOUNT1
        
        )
        
        ctx.cursor().execute('USE INDIA_SOCIAL_IMPACT_DATA_SET.HACKATHON')
        #cur = ctx.cursor().execute(query)


    except ProgrammingError as pr_ex:
        if pr_ex.errno == 1003:
            st.write(f"Programming error: {pr_ex}")
        elif pr_ex.errno == 90105:
            st.write('Connection Error')
            st.write(f"Programming error: {pr_ex}")
        elif pr_ex.errno == 2043:
            st.write('Connection Error')
            st.write(f"Programming error: {pr_ex}")
            
        else:
            raise
    finally:
        
        # con.close()


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