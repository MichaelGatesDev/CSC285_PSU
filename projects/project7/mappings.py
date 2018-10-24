#!/usr/bin/env python3

"""
Using the Basecamp module in conjunction with MatPlotLib we are going to create a map of New York state with your assigned cities mapped and labelled.

First, get the latitude and longitude of the place by making a web request to the MapQuest API with your city name
Use that latitude and longitude with the "annotate" method to create an annotation with the city name, and point to the location of the city with an arrow
"""


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

import mapquestapi


cities = ["wappingers falls village", "port chester village", "old westbury village"]
state = "NY"
key = "mJaEGNAdoNiCxWIE6ctXUocZSseutk5A"
mqapi = mapquestapi.MapQuestAPI(key)

for city in cities:
    (lat, long) = mqapi.getLatLong(cities[0], state)

place_data = [] # A placeholder for potential place information

# Create a new map of NY state
map = Basemap(resolution='h', projection='merc',
          lat_0=44.6995, lon_0=73.4529,
          llcrnrlon=-79.7619, llcrnrlat=40.4774, urcrnrlon=-71.7956, urcrnrlat=45.0159)

# Fill the globe with a blue color
map.drawmapboundary(fill_color='aqua')
# Fill the continents with the land color
map.fillcontinents(color='coral',lake_color='aqua')

# Read the information on states and counties from the shape files
map.readshapefile('shapes/st99_d00', name='states', linewidth=2)
map.readshapefile('shapes/cb_2017_us_county_20m', 'cb_2017_us_county_20m', color='blue')

# map.readshapefile('/home/whit4763/Downloads/st99_d00', name='states', linewidth=2)
# map.readshapefile('/home/whit4763/Downloads/cb_2017_us_county_20m/cb_2017_us_county_20m', 'cb_2017_us_country_20m', color='blue')

# Draw coast lines
map.drawcoastlines()

# collect the state names from the shapefile attributes so we can
# look up the shape obect for a state by it's name
state_names = []
for shape_dict in map.states_info:
    state_names.append(shape_dict['NAME'])

ax = plt.gca() # get current axes instance

# get NY and draw the filled polygon
seg = map.states[state_names.index('New York')]
poly = Polygon(seg, facecolor='white',edgecolor='black')
ax.add_patch(poly)

# I recommend using another for loop here to loop through the list you created with the relevant info
# but you could do it all in one for loop if youy want, use than "annotate" method here to draw your
# city information

plt.show()
