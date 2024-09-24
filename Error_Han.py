import os
import streamlit as st
import snowflake.connector
from snowflake.connector.errors import DatabaseError, ProgrammingError
from snowflake.snowpark import Session

PASSWORD = st.secrets["SPASSWORD"]
USER1 = st.secrets['SUSER1'] 
ACCOUNT1 = st.secrets['SACCOUNT1'] 


connection_params = {
    "account": ACCOUNT1,
    "user": USER1,
    "password": PASSWORD,
    "database":"INDIA_SOCIAL_IMPACT_DATA_SET",
    "schema": "HACKATHON"
    # "role":"ACCOUNTADMIN"
}

snowflake_account = ACCOUNT1
query = '''
SELECT * from HACKATHON.IDH_DATA
WHERE
    Identifier in ('SSEDUNIDUA11A') and Date between '2000-03-31' and  '2024-03-31' limit 1;
'''

try:
    con = snowflake.connector.connect(
        user=USER1,       # <-------- Bad user
        password=PASSWORD,   # <-------- Bad pass
        account=snowflake_account , # <-------- This is correct
        database="INDIA_SOCIAL_IMPACT_DATA_SET",
        schema= "HACKATHON"
    )
except DatabaseError as db_ex:
    if db_ex.errno == 250001:
        print(f"Invalid username/password, please re-enter username and password...")
        # code for user to re-enter username & pass
    else:
        raise
except Exception as ex:
    # Log this
    print(f"Some error you don't know how to handle {ex}")
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
        cur = ctx.cursor().execute(query)


    except ProgrammingError as pr_ex:
        if pr_ex.errno == 1003:
            print(f"Programming error: {pr_ex}")
        elif pr_ex.errno == 90105:
            print('disco')
            print(f"Programming error: {pr_ex}")
        elif pr_ex.errno == 2043:
            print('disco')
            print(f"Programming error: {pr_ex}")
            
        else:
            raise
    finally:
        print("Done")
        con.close()