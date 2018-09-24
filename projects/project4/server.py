#!/usr/bin/env python3
# Michael Gates
# 5 October 2018


from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import os
import stock_fetcher as StockUtils
import sqlite3


class DBHelper:

    def __init__(self, dbFile):
        self.db_file = dbFile

    """
    Creates the primary database for the program with structure:
    ----------------------------------
    | TEXT name  | TEXT abbreviation |
    ----------------------------------
    """
    def create_db(self):
        print("Creating database: " + self.db_file)
        con = sqlite3.connect(self.db_file)
        cursor = con.cursor()
        command = """CREATE TABLE IF NOT EXISTS stocks (
        name TEXT PRIMARY KEY,
        abbreviation TEXT
        );
        """
        cursor.execute(command)
        con.commit()
        con.close()
        print("Created database " + self.db_file)

    def insert(self, name, abbreviation):
        con = sqlite3.connect(self.db_file)
        cursor = con.cursor()
        command = "INSERT INTO stocks VALUES (\"" + name + "\", \"" + abbreviation + "\");"
        cursor.execute(command)
        con.commit()
        con.close()

    def try_insert(self, name, abbreviation):
        if(len(self.find(name)) > 0):
            return False
        self.insert(name, abbreviation)
        return True

    def find(self, name):
        con = sqlite3.connect(self.db_file)
        cursor = con.cursor()
        command = 'SELECT abbreviation FROM stocks WHERE name = "' + name + '";'
        cursor.execute(command)
        rows = cursor.fetchall()
        return rows if rows is not None else []

    def get_all(self):
        con = sqlite3.connect(self.db_file)
        cursor = con.cursor()
        command = 'SELECT * FROM people;'
        cursor.execute(command)
        rows = cursor.fetchall()
        return rows if rows is not None else []

class WebHandler(BaseHTTPRequestHandler):

    """
    Sets the content headers and response code required to function as an HTML page
    """
    def set_headers(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

    """
    Writes the provided *.html file to the web server.
    Supports sustitutions (e.g. {name} => 'bob')
    """
    def write_page(self, fileName, subs={}):
        if(not os.path.exists(fileName)):
            print("File does not exist!")
            self.error()
            return
        print("Writing web page " + fileName)
        self.set_headers()
        with open(fileName, 'r') as file:
            data = file.read().replace('\n', '')
            for keyword, sub in subs.items():
                data = data.replace(keyword.lower(), sub)
            self.wfile.write(bytes(data, "utf8"))
        print("Finished writing web page!")


    """
    Responds to GET requests to an endpoint of "price" with a query string parameter of "stock" and then will use BeautifulSoup to do a live lookup of that stock on Yahoo! stocks, MarketWatch, or another stock website of your choice and will return a textual response containing just the current price of the stock
    """
    def price(self, stock=''):
        stock = stock if len(stock) > 0 else 'N/A'
        sf = StockUtils.StockFetcher()
        if(stock == 'N/A'):
            self.write_page('stock_not_found.html', {'{stock}': stock})
            return

        value = 0
        try:
            value = sf.get_stock_value(stock)
        except Exception as e:
            print("Error parsing the page.")

        if(value == -1):
            self.write_page('stock_not_found.html', {'{stock}': stock})
        else:
            self.write_page('price.html', {'{stock}': stock, '{value}': str(value)})


    """
    Responds to GET requests to an endpoint of "name" with a query string parameter of "stock" and then uses either "sqlite3" or "pickle" modules to read the data of stock abbreviations to names and will return the company name based on the stock abbreviation passed in the URL (both the SQLite3 database file and a Pickle dictionary file will be provided to you and you can opt to use either one that suits you best.
    """
    def name(self, stock):
        sf = StockUtils.StockFetcher()
        if(stock == None):
            self.write_page('stock_not_found.html', {'{stock}': stock})
            return
        try:
            company = sf.get_company_name(stock)
        except Exception as e:
            print("Error parsing the page.")

        if(company == None):
            self.write_page('stock_not_found.html', {'{stock}': stock})
            return
        self.write_page('name.html', {'{stock}': stock, '{company}': company})


    """
    Responds to GET requests to an endpoint of "addStock" with two query string URL parameters "name", and "abbreviation" that will add the requested company name and abbreviation to the SQLite3 database or Pickle dictionary and return a "success" message if it is added or en "exists" error message if the stock was already present. The response can be text-based.
    """
    def add_stock(self, name, abbreviation):
        if(name is None or name == '' or abbreviation is None or abbreviation == ''):
            self.write_page('add_stock.html', {'{result}': 'failure'})
        else:
            if(dbhelper.try_insert(name, abbreviation)):
                self.write_page('add_stock.html', {'{result}': 'success'})
            else:
                self.write_page('add_stock.html', {'{result}': 'duplicate'})

    """
    Writes the default 'error' webpage
    """
    def error(self):
        self.write_page('error.html')

    def do_GET(self):

        parsed_path = parse.urlparse(self.path)
        real_path = parsed_path.path
        query = parsed_path.query # string
        queries = query.split('&')
        params = {}
        for query in queries:
            qs = query.split('=')
            if(len(qs) == 2):
                params[qs[0]] = qs[1]

        # /price?stock={}
        if(real_path == '/price'):
            stock = ''
            if('stock' in params):
                stock = params['stock']
            self.price(stock)
        # /name?stock={}
        elif(real_path == '/name'):
            stock = ''
            if('stock' in params):
                stock = params['stock']
            self.name(stock)
        # /addstock?name={}&abbreviation={}}
        elif(real_path == '/addstock'):
            name = params['name'] if 'name' in params else ''
            abbreviation = params['abbreviation'] if 'abbreviation' in params else ''
            if not 'name' in params or not 'abbreviation' in params:
                self.error()
                return
            self.add_stock(name, abbreviation)
        # anything else
        else:
            self.error()

stocks_file = 'stocks.db'
dbhelper = DBHelper(stocks_file)

"""
Main entry method
"""
if __name__ == '__main__':

    if(not os.path.exists(stocks_file)):
        dbhelper.create_db()

    print("Starting web server...")
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, WebHandler)
    print('Starting server, use <Ctrl-C> to stop')
    httpd.serve_forever()
