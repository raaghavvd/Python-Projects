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
fg= folium.FeatureGroup(name="Demo Map")
for lt, ln, el,loc in zip(data_lat,data_lon,data_elev,data_loc):

    fg.add_child(folium.Marker(location=[lt,ln],popup=loc + str(el)+"m",icon= folium.Icon(color=col_prod(el))))
map.add_child(fg)
map.save("map_app.html")
