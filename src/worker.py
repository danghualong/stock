import requests
from .model import Stock
from . import dboper
from . import const
from .parsers import historyParser, dailyPriceParser
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


def addHistoryDaily(days=180):
    items = dboper.getStocks()
    if (items is None):
        print("no stock fetched")
        return

    stop = datetime.datetime.now().strftime("%Y%m%d")
    start = (datetime.datetime.now() -
             datetime.timedelta(days=days)).strftime("%Y%m%d")
    print("{0}-{1} records will be inserted".format(start, stop))
    for item in items:
        details = _getDetails(item[0], start, stop)
        for detail in details:
            dboper.insertDaily(detail)
        print("----------{0}:{1} insert all daily records".format(
            item[0], item[1]))


def addDaily():
    items = dboper.getStocks()
    if (items is None):
        print("no stock fetched")
        return
    for item in items:
        daily = _getDetail("{0}{1}".format(item[2], item[0]))
        daily.code = item[0]
        dboper.insertDaily(daily, True)
        print("----------{0}:{1} insert one daily record".format(
            item[0], item[1]))


def _getDetails(code, start, stop):
    url = const.HISTORY_PRICE_URL.format(code, start, stop)
    resp = requests.get(url)
    content = resp.text
    details = historyParser.parse(content)
    return details


def _getDetail(code):
    url = const.DAILY_PRICE_URL.format(code)
    resp = requests.get(url)
    content = resp.text
    daily = dailyPriceParser.parse(content)
    return daily
