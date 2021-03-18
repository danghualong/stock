import requests
from ...constant import urls
from ...db import dboper
from ..parsers import jisuStockParser
from ...logger import currentLogger

def getStocks(pageNum):
    url=urls.JISU_STOCK_URL.format(pageNum)
    resp = requests.get(url)
    content = resp.text
    stocks = jisuStockParser.parse(content)
    if (stocks != None):
        for stock in stocks:
            dboper.insertStock(stock)
        currentLogger.info("page {0}, total {1} data are inserted".format(pageNum,len(stocks)))
    else:
        currentLogger.info("No stocks to insert")