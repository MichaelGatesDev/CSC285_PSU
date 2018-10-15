#!/usr/bin/env python3
# Michael Gates

from bs4 import BeautifulSoup
import urllib
import os


class CencusDownloader:

    def __init__(self):
        self.url = "https://www.census.gov/data/datasets/2017/demo/popest/total-cities-and-towns.html"
        self.__loadStates()


    def __loadStates(self):
        try:
            self.state_names = [i.lower() for i in open("states.txt").read().splitlines()]
            self.loadedStatesFile = True
        except:
            print("Unable to load states from file 'states.txt'. Resorting to fallback..")
            self.loadedStatesFile = False


    def isValidState(self, stateName):
        if not self.loadedStatesFile:
            page = urllib.request.urlopen(self.url).read()
            soup = BeautifulSoup(page, 'html.parser')
            uls = soup.findAll("ul", class_="uscb-margin-5 uscb-padding-LR-10 uscb-state-list-left")
            if len(uls) <= 0:
                print('"<ul>" elements not found')
                return
            for ul in uls:
                for li in ul.findAll('li'):
                    a = li.find('a')
                    if not a:
                        continue
                    if (a.contents != None and len(a.contents) >= 1):
                        name = str(a.contents[0]).strip()
                        if(name.lower() == stateName.lower()):
                            return True
        else:
            return stateName in self.state_names


    def download(self, stateName, fileName):
        page = urllib.request.urlopen(self.url).read()
        soup = BeautifulSoup(page, 'html.parser')

        uls = soup.findAll("ul", class_="uscb-margin-5 uscb-padding-LR-10 uscb-state-list-left")
        if len(uls) <= 0:
            print('"<ul>" elements not found')
            return
        dlurl = ""
        for ul in uls:
            for li in ul.findAll('li'):
                a = li.find('a')
                if not a:
                    continue
                if (a.contents != None and len(a.contents) >= 1):
                    name = str(a.contents[0]).lower().strip()
                    if(name == stateName):
                        dlurl = "https:" + a['href']
                        break
        if(len(dlurl) <= 0):
            print("Download URL invalid")
            return
        self.__do_download(dlurl, fileName)


    def __do_download(self, url, fileName):
        if not os.path.exists("downloads"):
            os.mkdir("downloads")
        path = os.path.join("downloads", fileName)
        if os.path.exists(path):
            print("Existing data file found.")
        else:
            print("Downloading data from '" + url + "' into file '" + fileName + "'...")
            urllib.request.urlretrieve(url, path)
            print("Download complete.")
