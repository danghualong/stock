from ...constant import urls
from ...db import dboper
from ..parsers import dailyPriceParser
from ...logger import currentLogger
import requests

def addDaily():
    stocks = dboper.getStocks()
    if (stocks is None or len(stocks)<=0):
        currentLogger.warn("no stock fetched")
        return
    for stock in stocks:
        daily = _getDetail("{0}{1}".format(stock.prefix, stock.code))
        daily.code = stock.code
        dboper.insertDaily(daily, True)
        currentLogger.info("----------{0}:{1} insert one daily record".format(
            stock.code, stock.name))

def _getDetail(code):
    url = urls.DAILY_PRICE_URL.format(code)
    resp = requests.get(url)
    content = resp.text
    daily = dailyPriceParser.parse(content)
    return daily
