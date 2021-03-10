from ...db import dboper
from ..util import trait_builder as TraitBuilder
from ..service import ma_service as MAService
from ..policies import ma_policy as MAPolicy


def selectStock(days=20,breakDays=1,maFastDays=5,maSlowDays=10):
    '''
    days:比较的天数
    breakDays:快线突破慢线的天数
    maFastDays:5日均线
    maSlowDays:10日均线
    '''
    results=[]
    stocks = dboper.getStocks()
    for stock in stocks:
        dailys = dboper.getDailys(stock.code, maSlowDays + days - 1)
        traits = []
        for daily in dailys:
            trait = TraitBuilder.populateTrait(daily)
            traits.append(trait)
        if (len(traits) < maSlowDays + days - 1):
            continue
        MAService.calcMA(traits, maFastDays)
        MAService.calcMA(traits, maSlowDays)
        if (MAPolicy.isTarget(traits,totalDays=days,breakDays=breakDays, maFastDays=maFastDays, maSlowDays=maSlowDays)):
            results.append({stock.code: stock.name})
    return results
 