from .. import dboper
from . import stat,table

def showCurrentTrends():
    stocks = dboper.getStocks()
    if (stocks is None or len(stocks)<=0):
        print("no stock fetched")
        return
    for stock in stocks:
        traits=stat.caclTrait(stock.code)
        table.showMAAndATR(traits, stock)
        word = input("点击q退出,其他键继续...\n")
        if (word == 'q'):
            break
        else:
            print(word)