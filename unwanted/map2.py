import pandas as pd
import plotly.express as px
import plotly
import json
import requests
from datetime import date
wiki_df =pd.read_html('https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India')[5].dropna(how='all',axis=1)
wiki_df = wiki_df.drop(wiki_df.tail(2).index)
wiki_df.columns = ['States','Cases','Deaths','Recovered','Active']
wiki_df['Cases'] = wiki_df['Cases'].apply(lambda x: x.split('[')[0]).apply(lambda x: x.replace(',',''))
wiki_df['Deaths'] = wiki_df['Deaths'].apply(lambda x: x.split('[')[0]).apply(lambda x: x.replace(',',''))
wiki_df.drop(17,inplace=True)
wiki_df['Date'] = date.today()
india_geojson = json.load(open("india_geojson.geojson", "r"))
state_id_map = {}
for feature in india_geojson["features"]:
feature["id"] = feature["properties"]["state_code"]
state_id_map[feature["properties"]["st_nm"]] = feature["id"]
wiki_df["id"] = wiki_df["States"].apply(lambda x: state_id_map[x])
wiki_df[['Active','Cases','Deaths','Recovered']] = wiki_df[['Active','Cases','Deaths','Recovered']].apply(pd.to_numeric)
fig = px.choropleth_mapbox(
wiki_df,
locations="id",
geojson=india_geojson,
color="Cases",
hover_name="States",
hover_data=["Cases","Active","Recovered","Deaths","Date"],
title="",
mapbox_style="carto-positron",
color_continuous_scale='Inferno_r',
center={"lat": 23, "lon": 88},
zoom=3.45,
opacity=1,
)
fig.update_layout(height=700, width=950, font=dict(family="Arial, Helvetica, sans-serif",size=24,), title_x=0.5, coloraxis_colorbar=dict(title="Covid cases"),)
fig.update_layout(coloraxis_colorbar_x=-0.25,)
fig.show()