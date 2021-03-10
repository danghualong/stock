import requests
from ...constant import urls
from ...db import dboper
from ..parsers import jisuStockParser

def getStocks(pageNum):
    url=urls.JISU_STOCK_URL.format(pageNum)
    resp = requests.get(url)
    content = resp.text
    stocks = jisuStockParser.parse(content)
    if (stocks != None):
        for stock in stocks:
            dboper.insertStock(stock)
        print("page {0}, total {1} data are inserted".format(pageNum,len(stocks)))
    else:
        print("No stocks to insert")