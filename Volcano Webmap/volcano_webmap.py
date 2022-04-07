#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing folium which is used for OpenStreetMap
import folium
import pandas 

# Loading the txt file using pandas and storing the columns needed to a list
data = pandas.read_csv('Volcanoes.txt')
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation< 1000:
        return 'green'
    elif 1000<= elevation <3000:
        return 'orange'
    else:
        return 'red'
map= folium.Map(location=[38.58,-99.09], zoom_start=6)

# Creating a feature group for folium
fgv = folium.FeatureGroup(name="Volcanoes")


# To iterate through the Longitude and Latitude lists from the dataframe using the zip function
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lat,lon] , radius = 6, popup=str(el) + " m", fill_color=color_producer(el), fill=True, color = 'grey', fill_opacity=0.7))

# Reading the json file using the GeoJson function
fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Maps.html")

