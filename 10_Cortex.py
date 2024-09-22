import os
# from dotenv import load_dotenv
import streamlit as st
from snowflake import connector
from snowflake.snowpark import Session
from snowflake.cortex import Summarize, Complete, ExtractAnswer, Sentiment, Translate
from snowflake import connector
from snowflake.snowpark import Session
import snowflake.connector
import pandas as pd
import string
import plotly.express as px

from dotenv import load_dotenv
import os
load_dotenv()
# PASSWORD = os.getenv('PASSWORD')
# USER2 = os.getenv('USER2')
# ACCOUNT2 = os.getenv('ACCOUNT2')

PASSWORD = st.secrets["SPASSWORD"]
USER2 = st.secrets['SUSER2'] 
ACCOUNT2 = st.secrets['SACCOUNT2'] 

st.set_page_config(page_title="App Feedback",
                   page_icon="💬",
                   )
st.title("Lets Use :red[Cortex]🤖 to Do Some Sentiment Analysis 🗣 and Fetch Some Ratings⭐⭐⭐⭐ for this App:")

connection_params = {
    "account": ACCOUNT2,
    "user": USER2,
    "password": PASSWORD
}

# Create a Snowflake session
snowflake_session = Session.builder.configs(connection_params).create()


# Define the LLM functions
def summarize(user_text):
    summary = Summarize(text=user_text, session=snowflake_session)
    return summary


def complete(user_text):
    completion = Complete(
        model="snowflake-arctic",
        prompt=f"Provide 5 keywords from the following text: {user_text}",
        session=snowflake_session,
    )
    return completion


def extract_answer(user_text):
    answer = ExtractAnswer(
        from_text=user_text,
        question="What is the Importance of Pupil-Teacher Ratios",
        session=snowflake_session,
    )
    return answer


def sentiment(user_text):
    sentiment = Sentiment(text=user_text, session=snowflake_session)
    return sentiment


def translate(user_text):
    translation = Translate(
        text=user_text, from_language="en", to_language="de", session=snowflake_session
    )
    return translation




user_text1 = """
        Keep up the good Work. Loved the information
    """


        # summary_result = summarize(user_text)
        # print(
        #     f"Summarize() Snowflake Cortex LLM function result:\n{summary_result.strip()}\n"
        # )

        # completion_result = complete(user_text)
        # print(
        #     f"Complete() Snowflake Cortex LLM function result:\n{completion_result.strip()}\n"
        # )

        # answer_result = extract_answer(user_text)
        # print(
        #     f"ExtractAnswer() Snowflake Cortex LLM function result:\n{answer_result}\n"
        # )

# sentiment_result = sentiment(user_text1)
# print(
#     f"Sentiment() Snowflake Cortex LLM function result:\n{sentiment_result}\n"
# )

        # translation_result = translate(user_text)
        # print(
        #     f"Translate() Snowflake Cortex LLM function result:\n{translation_result.strip()}\n"
        # )

with st.form("Input"):
    review = st.text_area("Submit Review about our website:", height=3, max_chars=100)
    
    
    submit = st.form_submit_button('Submit Review')
    btnResult = st.form_submit_button('View All the Reviews and Ratings')

if btnResult:
    # Create a Snowflake session
    session = Session.builder.configs(connection_params).create()
    ctx = snowflake.connector.connect(
    user=USER2,
    password=PASSWORD,
    account=ACCOUNT2
    
    
    )
    
    ctx.cursor().execute('USE SENTIMENT_DATA.PUBLIC')
    cur = ctx.cursor().execute('SELECT * FROM POLL')
    df = pd.DataFrame.from_records(iter(cur), columns=[x[0] for x in cur.description])
    df = df.drop(['ID', 'CREATED_AT'], axis=1)
    for index, row in df.iterrows():
            if (row['RATING']=='Highly Positive'):
                st.write("⭐⭐⭐⭐⭐⭐⭐⭐")
                st.write(row['REVIEW'])
            elif (row['RATING']=='Highly Negative'):
                st.write("⭐")
                st.write(row['REVIEW'])
            elif (row['RATING']=='Neutral'):
                st.write("⭐⭐")
                st.write(row['REVIEW'])
            elif (row['RATING']=='Negative'):
                st.write("⭐")
                st.write(row['REVIEW'])
            else:
                st.write("⭐⭐⭐⭐")
                st.write(row['REVIEW'])
            
    pie_data=df.groupby(['RATING']).size().reset_index(name='Count')
    st.subheader("The Final Report of Sentiment Analysis📋")
    fig = px.pie(pie_data, values='Count', names='RATING')
    st.plotly_chart(fig)
    st.write(df.style.background_gradient(cmap="Blues"))
    st.text('Fetched Results')
    snowflake_session.close()

    

if submit:
    # Create a Snowflake session
    
    session = Session.builder.configs(connection_params).create()
    ctx = snowflake.connector.connect(
    user=USER2,
    password=PASSWORD,
    account=ACCOUNT2
    
    
    )
    review=review.translate(str.maketrans('', '', string.punctuation))
    sentiment_result = sentiment(review)
    score=sentiment_result
    if (score>=0.6):
        rating='Highly Positive'
    elif (score <= -0.6):
        rating='Highly Negative'
    elif (score == 0):
        rating='Neutral'
    elif (-0.6 < score< 0):
        rating='Negative'
    else:
        rating='Positive'

    

    
    query_INS="INSERT INTO POLL (rating,review) VALUES ('"+rating+"','"+review+"');"
    ctx.cursor().execute('USE SENTIMENT_DATA.PUBLIC')
    ctx.cursor().execute(query_INS)
    snowflake_session.close()
    # run query
    # st.write(queryText)

# if snowflake_session:
#     # Close the Snowflake session
#     snowflake_session.close()


