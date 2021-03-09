from ..model import Trait
from .. import dboper
from ..policies import ma_policy as MAPolicy
import math

DAYS = 50

def _populateTrait(daily):
    trait = Trait()
    trait.date = daily.date
    trait.last_close=float(daily.last_close)
    trait.open = float(daily.open)
    trait.high = float(daily.high)
    trait.low = float(daily.low)
    trait.close = float(daily.current)
    return trait

def caclTrait(code,N=120):
    dailys = dboper.getDailys(code, DAYS + N - 1)
    traits=[]
    for daily in dailys:
        trait = _populateTrait(daily)
        traits.append(trait)
    calcATR(traits, 10)
    calcATR(traits, 20)
    calcMA(traits, 5)
    calcMA(traits, 10)
    calcMA(traits, 20)
    calcMA(traits, 30)
    calcMA(traits, 60)
    calcMA(traits, 120)
    return traits[-DAYS:]

def calcATR(traits,N=20):
    result=[]
    total = 0.0
    slowIndex = 0
    fastIndex = 0
    for fastIndex in range(len(traits)):
        trait=traits[fastIndex]
        if (fastIndex < N):
            total += trait.getTrueRange()
            trait.ATR[N]=total / (fastIndex + 1)
        else:
            total = total - traits[slowIndex].getTrueRange() + trait.getTrueRange()
            trait.ATR[N]=total/N
            slowIndex += 1

def calcMA(traits, N=5):
    result=[]
    total = 0.0
    slowIndex = 0
    fastIndex = 0
    for fastIndex in range(len(traits)):
        trait=traits[fastIndex]
        if (fastIndex < N):
            total += trait.close
            trait.MA[N] = total / (fastIndex + 1)
        else:
            total = total - traits[slowIndex].close + trait.close
            trait.MA[N]=total/N
            slowIndex += 1


def selectStock(days=20):
    results=[]
    stocks = dboper.getStocks()
    for stock in stocks:
        dailys = dboper.getDailys(stock.code, maxN + days - 1)
        traits = []
        for daily in dailys:
            trait = _populateTrait(daily)
            traits.append(trait)
        if (len(traits) < days):
            continue
        calcMA(traits, 5)
        calcMA(traits, 10)
        if (MAPolicy.isTarget(traits, breakDays=2, maSlow=5, maFast=10)):
            results.append({stock.code: stock.name})
    return results
        
        