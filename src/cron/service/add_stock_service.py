from ...model import Stock
from ...db import dboper

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
