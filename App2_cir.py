import folium
import pandas as pd
data= pd.read_csv("Volcanoes.txt")
data_lon=list(data["LON"])
data_lat=list(data["LAT"])
data_elev= list(data["ELEV"])
data_loc=list(data["LOCATION"])
def col_prod(elevation):
        if elevation < 1000:
            return 'green'
        elif 1000<=elevation<3000:
            return 'orange'
        else:
            return 'red'


map= folium.Map(location=[38.58,-99.09],tiles= "Mapbox Bright")
fgv= folium.FeatureGroup(name="Volcanoes")


for lt, ln, el,loc in zip(data_lat,data_lon,data_elev,data_loc):

    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius= 6, popup=loc + str(el)+"m",fill_color= col_prod(el) ,color= 'grey',fill= True ,fill_opacity=0.7))
fgp= folium.FeatureGroup(name="Population")


fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 1000000 else 'orange' if 1000000<= x['properties']['POP2005']<2000000 else 'red'}))
'''ß
fg.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 1000000}))
'''
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map_app.html")
