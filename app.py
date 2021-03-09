import src.stat.stat as stat
import src.stat.breakthrough as bt
import src.stat.table as table
import src.stat.trends as trends
from src.model import Stock


def ShowSingleMA(stock):
    traits = stat.caclTrait(stock.code)
    table.showMA(traits, stock, True)

def ShowSingleATR(stock):
    traits = stat.caclTrait(stock.code)
    table.showATR(traits, stock, True)

def ShowBreakThroughPoint(code):
    traits = stat.caclTrait(code)
    # 估计当天短线突破长线的当前价格
    btp = bt.getBreakThroughPoint(traits, 5, 10)
    print("ma5:{0},ma10:{1}".format(round(traits[-1].MA[5],3),round(traits[-1].MA[10],3)))
    print("BreakThroughPoint:{0}".format(round(btp,3)))

if __name__ == "__main__":
    # trends.showCurrentTrends()
    # stock = Stock()
    # stock.code = '300760'
    # stock.name="迈瑞医疗"
    # ShowSingleMA(stock)
    
