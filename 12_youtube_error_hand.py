import os
import pandas as pd
# from dotenv import load_dotenv
import streamlit as st
from snowflake import connector
from snowflake.snowpark import Session
from snowflake.connector.errors import DatabaseError, ProgrammingError

# Import the necessary module
from dotenv import load_dotenv
import os
load_dotenv()

# PASSWORD = os.getenv('PASSWORD')
# USER1 = os.getenv('USER1')
# ACCOUNT1 = os.getenv('ACCOUNT1')

PASSWORD = st.secrets["SPASSWORD"]
USER = st.secrets['SUSER'] 
ACCOUNT = st.secrets['SACCOUNT'] 
#########################################
st.set_page_config(page_title="Live Youtube Data",
                   page_icon="📥",
                   )

st.title("Lets Use\n :blue[BRIGHT_DATA YOUTUBE_PROFILES__POSTS__COMMENTS]💾 to View some Stats :")


st.write("""Youtube is one of the most widely used Platforms""")
st.write("""Below is a small Sample dataset which shows some Educational Platforms""")
st.write("""What it depicts is the fact that even independent creators can reach out to millions of people
         This basically indicates that e-learning is one of the most viable alternative to compensate for lower Taecher to Student Ratios""")
st.write("""Rainbow Junior is a channel for example which can be used for Pre primary education.
         With Independent Content Creators stepping in The dearth of Trained teachers can be Compensated for.""")
st.subheader("#️⃣Lets Fetch some Live stats📈")
st.subheader("🚩👣Steps to Use: Click on Fetch to Query Bright Data")
#########################################



query='''SELECT URL,HANDLE,NAME,SUBSCRIBERS,VIDEOS_COUNT,VIEWS,DESCRIPTION,DETAILS
FROM YOUTUBE_PROFILES__POSTS__COMMENTS.PUBLIC.YOUTUBE_PROFILES_NEW
where LOWER(name) like '%english%' or LOWER(name) like '%code%' or LOWER(name) like '%academy%' or LOWER(name) like '%edu%' or LOWER(name) like '%learn%';
'''

st.write("Query:", query)
connection_params = {
    "account": ACCOUNT,
    "user": USER,
    "password": PASSWORD,
    "database":"YOUTUBE_PROFILES__POSTS__COMMENTS",
    "schema": "PUBLIC",
    "role":"ACCOUNTADMIN"
}





import snowflake.connector
import pandas as pd

try:
    con = snowflake.connector.connect(
        user=USER,       # <-------- Bad user
        password=PASSWORD,   # <-------- Bad pass
        account=ACCOUNT, # <-------- This is correct
        database="YOUTUBE_PROFILES__POSTS__COMMENTS",
        schema= "PUBLIC"
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
        user=USER,
        password=PASSWORD,
        account=ACCOUNT
        
        )
        
        ctx.cursor().execute('USE INDIA_SOCIAL_IMPACT_DATA_SET.PUBLIC')
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
            btnResult = st.form_submit_button('Fetch Latest Data')

        if btnResult:
            # Create a Snowflake session
            session = Session.builder.configs(connection_params).create()
            ctx = snowflake.connector.connect(
            user=USER,
            password=PASSWORD,
            account=ACCOUNT
            
            )
            
            #ctx.cursor().execute('USE YOUTUBE_PROFILES__POSTS__COMMENTS.PUBLIC')
            cur = ctx.cursor().execute(query)
            df = pd.DataFrame.from_records(iter(cur), columns=[x[0] for x in cur.description])
            st.write(df.style.background_gradient(cmap="Blues"))
            st.text('Fetched Results')


        df_stats = pd.read_csv(f'youtube/YouTube Profiles & Posts & Comments - Examples Bright_Data.csv')
        st.write(df_stats.style.background_gradient(cmap="Blues"))
            
        