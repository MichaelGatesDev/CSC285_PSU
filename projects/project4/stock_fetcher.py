#!/usr/bin/env python3
# Michael Gates
# 5 October 2018

from bs4 import BeautifulSoup
import urllib

class StockFetcher:

    def __init__(self):
        self.url = "https://www.marketwatch.com/investing/stock/"

    def get_stock_value(self, stock):
        page = urllib.request.urlopen(self.url + stock).read()
        soup = BeautifulSoup(page, 'html.parser')
        h3 = soup.find("h3", class_="intraday__price")
        if h3:
            bq = h3.find('bg-quote', class_='value')
            if(bq != None and bq.contents != None and len(bq.contents) >= 1):
                return bq.contents[0]
        return -1


    def get_company_name(self, stock):
        page = urllib.request.urlopen(self.url + stock).read()
        soup = BeautifulSoup(page, 'html.parser')
        h1 = soup.find("h1", class_="company__name")
        if (h1 and h1.contents != None and len(h1.contents) >= 1):
            return h1.contents[0]
        return None
