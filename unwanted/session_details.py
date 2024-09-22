import os
# from dotenv import load_dotenv

from snowflake import connector
from snowflake.snowpark import Session
from snowflake.cortex import Summarize, Complete, ExtractAnswer, Sentiment, Translate

# Load environment variables from .env
# load_dotenv()

connection_params = {
    "account": "sibsego-vub12130",
    "user": "mrinalsnow2",
    "password": "passSNOW@1234",
    "database":"CC_QUICKSTART_CORTEX_DOCS",
    "schema": "DATA"
    # "role":"ACCOUNTADMIN"
}


# Create a Snowflake session
session = Session.builder.configs(connection_params).create()


# Create a Snowflake session
snowflake_session = Session.builder.configs(connection_params).create()

print("Account",snowflake_session.get_current_account())
print(snowflake_session.get_current_database())
print(snowflake_session.get_current_schema())
print(snowflake_session.get_current_role())
print(snowflake_session.get_current_warehouse())
print(snowflake_session.get_fully_qualified_current_schema())