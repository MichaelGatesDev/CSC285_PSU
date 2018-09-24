# Project 4

##

## Instructions

1. Open a shell terminal and type the following command from within the directory of the program
> python3 server.py

2. In a web browser, navigate to `localhost:8080`

3. You should see a page like this:
![Ran into a server issue! Try again later.](http://i.imgur.com/zAoVMgK.png)

4. You can now change the URL parameters to receive different [served] results

## Paths

### GET `/price?stock=STOCK_NAME_HERE`

This will fetch the stock price for the given stock and return a page like this if it is successful

![](http://i.imgur.com/iXk70jZ.png)

or like this if it is not successful

![](http://i.imgur.com/P8Db8ve.png)


### GET `/name?stock=STOCK_NAME_HERE`

This will fetch the company name for the given stock and return a page like this if it is successful

![](http://i.imgur.com/q9JqAxk.png)

or like this if it is not successful

![](http://i.imgur.com/F8LUf2Q.png)
