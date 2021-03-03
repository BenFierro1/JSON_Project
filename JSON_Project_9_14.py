import json

infile = open("US_fires_9_14.json", "r")
outfile = open("readable_fire_data2.json", "w")
# this json.load()takes json file and converts it into a usable python file
# in this case, its a giant dictionary
fire_data = json.load(infile)
# json.dump() takes json data object and a file object, and put it in a
# file to specify indent level of 4
json.dump(fire_data, outfile, indent=4)

lists_of_fires = fire_data[:]

brightness, lons, lats = [], [], []


for fire in lists_of_fires:
    bright = fire["brightness"]
    lon = fire["longitude"]
    lat = fire["latitude"]
    if bright > 450:
        brightness.append(bright)
        lons.append(lon)
        lats.append(lat)

print(brightness[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": 10,
            "color": brightness,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

lat_foc = 40
lon_foc = -112
my_layout = Layout(
    title="US Fires - 9/14/2020 through 9/20/2020",
    geo=dict(projection_scale=7.1, center=dict(lat=lat_foc, lon=lon_foc)),
)

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_fires_9_14.html")
