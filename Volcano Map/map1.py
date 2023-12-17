import folium
import pandas


data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'Green'
    elif 1000 <= elevation < 3000:
        return 'White'
    else:
        return 'Red'

map = folium.Map(location = [38.58, -99.09],zoom_start = 6, tiles = "CartoDB dark_matter")

fgv = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 10, popup = str(el), tooltip = str(el) + " M",
    color = color_producer(el), fill_opacity=10))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor':'blue' if x['properties']['POP2005'] < 10000000
else 'white' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'black'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
