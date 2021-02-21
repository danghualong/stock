from ..model import Trait
from .. import dboper
import math

DAYS = 50

def caclTrait(code,N=120):
    dailys = dboper.getDailys(code, DAYS + N - 1)
    traits=[]
    for daily in dailys:
        trait = Trait()
        trait.date = daily.date
        trait.last_close=float(daily.last_close)
        trait.open = float(daily.open)
        trait.high = float(daily.high)
        trait.low = float(daily.low)
        trait.close = float(daily.current)
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
