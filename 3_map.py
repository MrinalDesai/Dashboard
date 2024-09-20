import folium
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import branca.colormap as cm

st.set_page_config(page_title="Map",page_icon="🗺️",)
json1 = f"states_india.geojson"

m = folium.Map(location=[23.47, 77.94], tiles='Cartodbdark_matter',name="Light Map",
           zoom_start=5,
           
           attr='My Data Attribution',
                        width=900,
                        height=800)
#CartoDB positron

india_covid = f"covid_cases_india.csv"
india_covid_data = pd.read_csv(india_covid)


choice = ['Confirmed Cases','Active Cases', 'Cured/Discharged', 'Death']
choice_selected = st.selectbox("Select Choice ", choice)
folium.Choropleth(
    geo_data=json1,
    name="choropleth",
    data=india_covid_data,
    columns=["state_code", choice_selected],
    key_on="feature.properties.state_code",
    fill_color="YlGn",#"YlOrRd",
    color="black",
    
    fill_opacity=0.7,
    line_opacity=.001,
    legend_name=choice_selected+"(%)",
).add_to(m)


folium.features.GeoJson('states_india.geojson', name="LSOA Code",
                           popup=folium.features.GeoJsonPopup(fields=['st_nm',])).add_to(m)
folium.FeatureGroup(name="Your Text Here",overlay=True,control=True)
folium_static(m, width=1200, height=950)