#!/usr/bin/env python3

import requests
import os
import json


#   https://www.mapquestapi.com/geocoding/v1/address?key=KEY&inFormat=kvp&outFormat=json&location=old+westbury+village%2C+NY&thumbMaps=false

class MapQuestAPI:

    def __init__(self, key):
        self.key = key
        self.base_url = "http://www.mapquestapi.com/geocoding/v1/address?key=" + self.key +  "&inFormat=kvp&outFormat=json"

    def getLatLong(self, city, state):
        city = city.strip().replace(" ", "%20")
        state = state.strip().replace(" ", "%20")
        url = self.base_url + "&location=" + city + "%2C+" + state + "&thumbMaps=false"
        print(f"Opening page: {url}")
        content = requests.get(url)
        data = json.loads(content.text)

        results = data['results'] # "results"
        if(len(results) < 1):
            return
        locations = results[0]['locations']
        if(len(locations) < 1):
            return
        loc = locations[0]
        locState = loc["adminArea3"]
        locCity = loc["adminArea5"]
        lat = loc["latLng"]["lat"]
        long = loc["latLng"]["lng"]
        print(f"State: {locState}, City: {locCity}, Lat: {str(lat)}, Long: {str(long)}")
        return (lat, long)
