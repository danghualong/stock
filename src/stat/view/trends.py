from ...db import dboper
from . import table
from ..service import trait_service as TraitService 

def showCurrentTrends():
    stocks = dboper.getStocks()
    if (stocks is None or len(stocks)<=0):
        print("no stock fetched")
        return
    for stock in stocks:
        traits=TraitService.getTraits(stock.code)
        table.showMAAndATR(traits, stock)
        word = input("点击q退出,其他键继续...\n")
        if (word == 'q'):
            break
        else:
            print(word)