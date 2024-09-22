import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    "1_about_me.py",
    title="Introduction",
    
    default=True,
)


project_1_page = st.Page(
    "2_T_P_Ratio.py",
    title="👨🏻‍🏫Teacher to 👩🏻‍🎓Pupil Ratio",
    
)
project_2_page = st.Page(
    "3_Map1.py",
    title="🗺️Map:Pupil/Teacher-Statewise🗺️",
    
)

project_3_page = st.Page(
    "cortex_3_error_hand.py",
    title="🧠Lets Ask Cortex Q&A",
    
)

project_4_page = st.Page(
    "10_Cortex_error_hand.py",
    title="💬FeedBack Sentiment Analysis",
   
)

project_5_page = st.Page(
    "9_live_data_error_hand.py",
    title="📥Live Data",
    
)

project_6_page = st.Page(
    "8_Funds.py",
    title="💵Funds",
    
)

project_7_page = st.Page(
    "7_Infra.py",
    title="🌍Digital-Infra/Peer-Learning",
   
)

project_8_page = st.Page(
    "6_Training.py",
    title="📖Training",
    
)

project_9_page = st.Page(
    "5_Nos.py",
    title="👩🏻‍🏫Teacher Statistics",
    
)

project_10_page = st.Page(
    "4_internet.py",
    title="🌍Internet",
    
)

project_11_page = st.Page(
    "12_youtube_error_hand.py",
    title="🛑LIVE 🎞️🎥Youtube",
    
)

project_12_page = st.Page(
    "58_Prediction.py",
    title="📊Forecast",
    
)


project_14_page = st.Page(
    "14_Insights_Recommendation.py",
    title="💡Insights",
    
)

project_15_page = st.Page(
    "15_Blended_learning.py",
    title="📚Blended Learning",
    
)


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Teacher Stats": [project_1_page, project_2_page,project_9_page,project_5_page,project_12_page],
        "Solution": [project_8_page, project_6_page,project_10_page,project_7_page,project_11_page,project_15_page],
        "AI": [ project_3_page],
         "Final Section": [project_4_page,project_14_page],

        # "Info": [about_page],
        # "Teacher Stats": [project_1_page, project_2_page,project_3_page],
        # "Solution": [project_4_page, project_5_page,project_6_page],
        # "AI": [project_7_page, project_8_page,project_9_page],
        # "Final Section": [project_10_page, project_11_page,project_12_page],
    }
)



# --- RUN NAVIGATION ---
pg.run()