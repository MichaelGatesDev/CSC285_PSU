#!/usr/bin/env python3
# Michael Gates
# 17 October 2018


# https://docs.scipy.org/doc/numpy-1.15.1/user/quickstart.html
# https://www.census.gov/data/datasets/2017/demo/popest/total-cities-and-towns.html

# import matplotlib as mpl
import os
import matplotlib.pyplot as plt
import numpy as np
import random
import math

import cencusweb
import popdata

mpl_markers = ".ov^<>8spP*hH+xXDd"

def randomShape():
    return random.choice(mpl_markers)

class Program:

    def __init__(self):
        self.selectedState = None
        self.downloader = cencusweb.CencusDownloader()

    """
    Asks the user to input the name of a state.
    If the state is valid, it will download the data from the web or load it from the disk.
    Returns true if the state is valid
    """
    def askState(self):
        state = input("Enter the name of a state in the US to download the cencus data for: ").lower()
        stateFileName = state.replace(" ", "-") + ".csv"
        if not self.downloader.isValidState(state):
            print("Could not find a state with the name '"  + state + "'")
            self.selectedState = None
            self.stateFileName = None
            return False
        self.downloader.download(state, stateFileName)
        self.selectedState = state
        self.stateFileName = stateFileName
        return True

    """
    Asks the user to input the name of a city/town
    Asks the user n number of times
    Takes StatePopulationData variable to validate city
    Returns the list of valid cities
    """
    def askCities(self, n, data):
        cities = []
        for i in range(0, n):
            city = input(f"Enter city #{i+1}: ").lower()
            while not data.isValidCity(city):
                print("Specified city is not valid.")
                city = input(f"Enter city #{i+1}: ").lower()
            cities.append(city)
        return cities

    def showPlot(self, data):
        t1 = list(np.arange(2010, 2018)) # 2010-2017
        cities = []
        minY = None
        maxY = None
        for d in data:
            if(len(d) < 2):
                continue
            city = d[0]
            dl = d[1]
            cities.append(city.title())
            p = plt.plot(t1, np.array(dl), marker=randomShape())
            if(not minY or min(dl) < minY):
                minY = min(dl)
            if(not maxY or max(dl) > maxY):
                maxY = max(dl)

        print(f"min is {str(minY)}")
        print(f"max is {str(maxY)}")
        n = (maxY - minY) / len(data)
        if(n < 100):
            n = 10
        elif(n < 1000):
            n = 100
        elif(n < 10000):
            n = 1000
        elif(n < 100000):
            n = 10000
        elif(n < 1000000):
            n = 100000
        print(f"Step rate: {n}")

        plt.yticks(np.arange(0, maxY+n, step=n)) # magic numbers
        plt.xlabel("Years")
        plt.ylabel("Population")
        plt.title(f"Populations within {self.state}")
        plt.legend(cities)
        plt.show()

    """
    The main entrypoint to the program
    """
    def main(self):

        run_as_project = True # <---------------------------------------------------------------------- CHANGE THIS

        if(run_as_project):
            ## ------------------------------------- ##
            ## HARDCODED AS PER PROJECT REQUIREMENTS ##
            self.selectedState = "New York" # <-------------------------------------------------------- CHANGE THIS
            self.stateFileName = "new-york.csv" # <---------------------------------------------------- CHANGE THIS
            ## ------------------------------------- ##
        else:
            # Ask for the state and grab the data
            while not self.selectedState:
                self.selectedState = self.askState()

        # Load the data for the state
        data = popdata.loadPopDataFromCSV(os.path.join("downloads", self.stateFileName))
        self.state = data.name

        if(run_as_project):
            ## ------------------------------------- ##
            ## HARDCODED AS PER PROJECT REQUIREMENTS ##
            num = 3 # <-------------------------------------------------------------------------------- CHANGE THIS
            cities = ["wappingers falls village", "port chester village", "old westbury village"] # <-- CHANGE THIS
            ## ------------------------------------- ##
        else:
            # Ask the user for the cities
            num = None
            while not num:
                try:
                    num = int(input("How many cities would you like to view? "))
                except ValueError:
                    print("Invalid number of cities.")

            cities = self.askCities(num, data)

        cd = []
        for c in cities:
            dataList = data.cityDataAsList(c)
            cd.append((c, dataList))
            # print(f"City: {c}")
            # print(f"Pops: {str(dataList)}")
        self.showPlot(cd)

def main():
    p = Program()
    p.main()

if __name__ == '__main__':
    main()
