import json

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")
# this json.load()takes json file and converts it into a usable python file
# in this case, its a giant dictionary
eq_data = json.load(infile)
# json.dump() takes json data object and a file object, and put it in a
# file to specify indent level of 4
json.dump(eq_data, outfile, indent=4)

lists_of_eqs = eq_data["features"]

mags, lons, lats = [], [], []


for eq in lists_of_eqs:
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes.html")
