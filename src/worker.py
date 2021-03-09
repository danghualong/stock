import requests
from .model import Stock
from . import dboper
from . import const
from .parsers import historyParser, dailyPriceParser,jisuStockParser
import datetime



def addStocks():
    stocks = [
        ('603288', "海天味业", "sh"),
        ('601012', "隆基股份", "sh"),
        ('600519', "贵州茅台", "sh"),
        ('600309', "万华化学", "sh"),
        ('600031', "三一重工", "sh"),
        ('600276', "恒瑞医药", "sh"),
        ('600887', "伊利股份", "sh"),
        ('601318', "中国平安", "sh"),
        ('601888', "中国中免", "sh"),
        ('603259', "药明康德", "sh"),
        ('600036', "招商银行", "sh"),
        ('002352', "顺丰控股", "sz"),
        ('002714', "牧原股份", "sz"),
        ('000858', "五粮液", "sz"),
        ('002475', "立讯精密", "sz"),
        ('000333', "美的集团", "sz"),
        ('002594', "比亚迪", "sz"),
        ('300015', "爱尔眼科", "sz"),
        ('300750', "宁德时代", "sz"),
        ('300760', "迈瑞医疗", "sz"),
        ('300059', "东方财富", "sz"),
    ]
    for item in stocks:
        stock = Stock()
        stock.code = item[0]
        stock.name = item[1]
        stock.prefix = item[2]
        dboper.insertStock(stock)
    print("add all stocks successfully")


def addHistoryDaily(days=300):
    stocks = dboper.getStocks()
    if (stocks is None or len(stocks)<=0):
        print("no stock fetched")
        return

    stop = datetime.datetime.now().strftime("%Y%m%d")
    start = (datetime.datetime.now() -
             datetime.timedelta(days=days)).strftime("%Y%m%d")
    print("{0}-{1} records will be inserted".format(start, stop))
    for stock in stocks:
        details = _getDetails(stock.code, start, stop)
        if (details is None):
            continue
        for detail in details:
            dboper.insertDaily(detail)
        print("----------{0}:{1} insert all daily records".format(
            stock.code, stock.name))


def addDaily():
    stocks = dboper.getStocks()
    if (stocks is None or len(stocks)<=0):
        print("no stock fetched")
        return
    for stock in stocks:
        daily = _getDetail("{0}{1}".format(stock.prefix, stock.code))
        daily.code = stock.code
        dboper.insertDaily(daily, True)
        print("----------{0}:{1} insert one daily record".format(
            stock.code, stock.name))


def _getDetails(code, start, stop):
    url = const.HISTORY_PRICE_URL.format(code, start, stop)
    resp = requests.get(url)
    content = resp.text
    details=None
    try:
        details = historyParser.parse(content)
    except Exception as ex:
        print("**********code:{0} error*************".format(code))
        print(ex)
    return details


def _getDetail(code):
    url = const.DAILY_PRICE_URL.format(code)
    resp = requests.get(url)
    content = resp.text
    daily = dailyPriceParser.parse(content)
    return daily


def getStocks(pageNum):
    url=const.JISU_STOCK_URL.format(pageNum)
    resp = requests.get(url)
    content = resp.text
    stocks = jisuStockParser.parse(content)
    if (stocks != None):
        for stock in stocks:
            dboper.insertStock(stock)
        print("page {0}, total {1} data are inserted".format(pageNum,len(stocks)))
    else:
        print("No stocks to insert")