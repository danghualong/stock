import json
from ..model import Stock



def parse(content):
    data = json.loads(content)
    status = data["status"]
    if (status != 0):
        return None
    stocks = []
    items = data['result']['list']
    for item in items:
        stock = Stock()
        stock.code = item["code"]
        stock.name = item["name"]
        stocks.append(stock)
    return stocks
