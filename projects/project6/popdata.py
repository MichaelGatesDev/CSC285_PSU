#!/usr/bin/env python3
# Michael Gates

import csv

class StatePopulationData:

    def __init__(self):
        self.name = None
        self.data = {} # (city, (year, pop))

    def addCity(self, name, year, pop):
        if not name in self.data:
            self.data[name] = {}
        self.data[name][year] = int(pop)
        # print(f"Added {name} {year} {pop} to {self.name}")

    def isValidCity(self, name):
        return name and name in self.data

    def cityCount(self):
        return len(self.data)

    def cityDataAsList(self, city):
        arr = []
        data = self.data[city]
        for k in data.keys():
            value = data[k]
            # print(f"Key: {k}, Value: {value}")
            arr.append(value)
        return arr

"""
NAME
POPESTIMATE2010
...
POPESTIMATE2017
"""
def loadPopDataFromCSV(file):
    print(f"Loading population data from {file}")
    with open(file) as csv_file:
        spd = StatePopulationData()
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                if not spd.name:
                    spd.name = row["STNAME"]
                city = row['NAME']
                if not city in spd.data:
                    for i in range(2010, 2018):
                        year = i
                        pop = row[f'POPESTIMATE{year}']
                        spd.addCity(city.lower(), year, pop)
                        # print(f"Population of {city} in {year} was {pop}")
            line_count += 1
        print(f"Loaded population data for {spd.cityCount()} cities in {spd.name}")
        return spd
