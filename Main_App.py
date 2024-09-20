import streamlit as st
# import base64

# def get_img_as_base64(file):
#     with open(file, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()


# img = get_img_as_base64("image.jpg")

# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] > .main {{
# background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
# background-size: 180%;
# background-position: top left;
# background-repeat: no-repeat;
# background-attachment: local;
# }}

# [data-testid="stSidebar"] > div:first-child {{
# background-image: url("data:image/png;base64,{img}");
# background-position: center; 
# background-repeat: no-repeat;
# background-attachment: fixed;
# }}

# [data-testid="stHeader"] {{
# background: rgba(0,0,0,0);
# }}

# [data-testid="stToolbar"] {{
# right: 2rem;
# }}
# </style>
# """
# st.markdown(page_bg_img, unsafe_allow_html=True)
# --- PAGE SETUP ---
about_page = st.Page(
    "1_about_me.py",
    title="About Me",
    #icon=":material/account_circle:",
    default=True,
)

# back_page = st.Page(
#     "Background.py",
#     title="About Me",
#     #icon=":material/account_circle:",
#     default=True,
# )
project_1_page = st.Page(
    "2_T_P_Ratio.py",
    title="👨🏻‍🏫Teacher to 👩🏻‍🎓Pupil Ratio",
    #icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "3_Map1.py",
    title="🗺️Map:Pupil/Teacher-Statewise🗺️",
    #icon=":material/smart_toy:",
)

project_3_page = st.Page(
    "cortex_3.py",
    title="Lets Ask Cortex🧠 Q&A",
    #icon=":material/smart_toy:",
)

project_4_page = st.Page(
    "10_Cortex.py",
    title="💬FeedBack Sentiment Analysis",
    #icon=":material/smart_toy:",
)

project_5_page = st.Page(
    "9_live_data.py",
    title="📥Live Data",
    #icon=":material/smart_toy:",
)

project_6_page = st.Page(
    "8_Funds.py",
    title="💵Funds",
    #icon=":material/smart_toy:",
)

project_7_page = st.Page(
    "7_Infra.py",
    title="🌍Internet Infrastructure",
    #icon=":material/smart_toy:",
)

project_8_page = st.Page(
    "6_Training.py",
    title="📖Training",
    #icon=":material/smart_toy:",
)

project_9_page = st.Page(
    "5_Nos.py",
    title="👩🏻‍🏫Teacher Statistics",
    #icon=":material/smart_toy:",
)

project_10_page = st.Page(
    "4_internet.py",
    title="🌍Internet",
    #icon=":material/smart_toy:",
)





# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
#pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page,project_3_page],
        "Remaining": [project_4_page, project_5_page,project_6_page],
        "Remaining2": [project_7_page, project_8_page,project_9_page],
        "Last": [project_10_page],
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")
# st.sidebar.markdown("Made with ❤️ by [Sven](https://youtube.com/@codingisfun)")


# --- RUN NAVIGATION ---
pg.run()