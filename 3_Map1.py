import folium
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import branca.colormap as cm
import geopandas as gpd


st.header('Student👩🏻‍🎓 to Teacher👨🏻‍🏫 Distribution Across States')
st.write("""Select the year to view the Distribution Accross states. Hover over the state to Find Individual Nos
         and select Primary-Higer Secondary from the Map Layers
         """)

fname = 'states_india.geojson'
nil = gpd.read_file(fname)

india_states = json1 = f"states_india.geojson"

df = pd.read_csv('State UT and School-wise Pupil teacher ratio (PTR) for 2008-2022 - Map.csv')
df[' Primary (1 to 5)'] = df[' Primary (1 to 5)'].fillna(df.groupby('st_nm')[' Primary (1 to 5)'].transform('mean'))
df['Higher Secondary (11-12)'] = df['Higher Secondary (11-12)'].fillna(df.groupby('st_nm')['Higher Secondary (11-12)'].transform('mean'))
df['Secondary (9-10)'] = df['Secondary (9-10)'].fillna(df.groupby('st_nm')['Secondary (9-10)'].transform('mean'))
df['Upper Primary (6-8)'] = df['Upper Primary (6-8)'].fillna(df.groupby('st_nm')['Upper Primary (6-8)'].transform('mean'))

year = df['Year'].unique().tolist()  
default_ix = year.index('2021-2022')
year_sel=st.selectbox('Select Year:',year,placeholder="Select a Option to Display Data",index=default_ix)
mask_year = (df['Year']==year_sel)
small=df[mask_year]
nilpop=nil.merge(small,on="st_nm")
#nilpop=gpd.read_file("output.geojson")

#m = folium.Map([43, -100], zoom_start=4)
m = folium.Map(location=[23.47, 77.94],zoom_start=5)
folium.Choropleth(name="Higher Secondary",
    geo_data=india_states,
    data=small,
    columns=["state_code", "Higher Secondary (11-12)"],
    fill_color="YlGn",
    key_on="feature.properties.state_code",
    legend_name="Higher Secondary (11-12)",
    show=True
    
).add_to(m)

folium.Choropleth(name="Secondary (9-10)",
    geo_data=india_states,
    data=small,
    columns=["state_code", "Secondary (9-10)"],
    fill_color="YlGn",
    key_on="feature.properties.state_code",
    legend_name="Secondary (9-10)",
    show=True
    
).add_to(m)

folium.Choropleth(name="Upper Primary (6-8)",
    geo_data=india_states,
    data=small,
    columns=["state_code", "Upper Primary (6-8)"],
    fill_color="YlGn",
    key_on="feature.properties.state_code",
    legend_name="Upper Primary (6-8)",
    show=True
    
).add_to(m)

folium.Choropleth(name=" Primary (1 to 5)",
    geo_data=india_states,
    data=small,
    columns=["state_code", " Primary (1 to 5)"],
    fill_color="YlGn",
    key_on="feature.properties.state_code",
    legend_name=" Primary (1 to 5)",
    show=True
    
).add_to(m)


style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}
NIL=folium.features.GeoJson(nilpop,
    style_function=style_function, 
    control=False,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['st_nm','Higher Secondary (11-12)','Secondary (9-10)',"Upper Primary (6-8)"," Primary (1 to 5)"],
        aliases=['State Name','Higher Secondary (11-12)','Secondary (9-10)',"Upper Primary (6-8)"," Primary (1 to 5)"],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")))


# folium.features.GeoJson('states_india.geojson', name="LSOA Code",zoom_on_click=True,
#                            popup=folium.features.GeoJsonPopup(fields=['st_nm',])).add_to(m)



# folium.Choropleth(name="Layer 2",
#     geo_data=india_states,
#     fill_opacity=0.3,
#     line_weight=2,
# ).add_to(m)
m.add_child(NIL)
m.keep_in_front(NIL)

folium.LayerControl(collapsed=False).add_to(m)

folium_static(m, width=900, height=950)