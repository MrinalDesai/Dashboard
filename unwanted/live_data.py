import os
# from dotenv import load_dotenv

from snowflake import connector
from snowflake.snowpark import Session


connection_params = {
    "account": "sltfmgk-dp79513",
    "user": "mrinalsnow1",
    "password": "passSNOW@1234",
    "database":"INDIA_SOCIAL_IMPACT_DATA_SET",
    "schema": "HACKATHON"
    # "role":"ACCOUNTADMIN"
}


# Create a Snowflake session
session = Session.builder.configs(connection_params).create()


import snowflake.connector
import pandas as pd

# Gets the version
ctx = snowflake.connector.connect(
    user="mrinalsnow1",
    password="passSNOW@1234",
    account="sltfmgk-dp79513"
    
    )
#ctx.cursor().execute('USE warehouse MY_WH')
ctx.cursor().execute('USE INDIA_SOCIAL_IMPACT_DATA_SET.HACKATHON')


query = '''
SELECT * from HACKATHON.IDH_DATA
WHERE
    Identifier in ('SSEDUNIDUA11A') and Date between '2000-03-31' and  '2024-03-31';
'''

cur = ctx.cursor().execute(query)
df = pd.DataFrame.from_records(iter(cur), columns=[x[0] for x in cur.description])

df.to_excel('wow.xlsx')