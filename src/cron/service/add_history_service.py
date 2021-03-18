from ...constant import urls
from ...db import dboper
from ..parsers import historyParser
from ...logger import currentLogger
import datetime
import requests


def addHistoryDaily(days=300):
    stocks = dboper.getStocks()
    if (stocks is None or len(stocks)<=0):
        currentLogger.warn("no stock fetched")
        return

    stop = datetime.datetime.now().strftime("%Y%m%d")
    start = (datetime.datetime.now() -
             datetime.timedelta(days=days)).strftime("%Y%m%d")
    currentLogger.info("{0}-{1} records will be inserted".format(start, stop))
    index=0
    for stock in stocks:
        details = _getDetails(stock.code, start, stop)
        index += 1
        if (details is None):
            continue
        for detail in details:
            dboper.insertDaily(detail)
        currentLogger.info("-------{2}/{3}---{0}:{1} insert all daily records".format(
            stock.code, stock.name,index,len(stocks)))

def _getDetails(code, start, stop):
    url = urls.HISTORY_PRICE_URL.format(code, start, stop)
    resp = requests.get(url)
    content = resp.text
    details=None
    try:
        details = historyParser.parse(content)
    except Exception as ex:
        currentLogger.error("code:{0} error \n%s",ex)
    return details
