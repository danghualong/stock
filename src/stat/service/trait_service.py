from ...db import dboper
from ..util import trait_builder as TraitBuilder
from . import atr_service as ATRService
from . import ma_service as MAService
import math

def getTraits(code, days=50, N=120):
    '''
    计算股票的汇总特征

    code:股票代码
    days:观察数据数量
    N:均值的天数
    '''
    dailys = dboper.getDailys(code, days + N - 1)
    traits=[]
    for daily in dailys:
        trait = TraitBuilder.populateTrait(daily)
        traits.append(trait)
    ATRService.calcATR(traits, 10)
    ATRService.calcATR(traits, 20)
    MAService.calcMA(traits, 5)
    MAService.calcMA(traits, 10)
    MAService.calcMA(traits, 20)
    MAService.calcMA(traits, 30)
    MAService.calcMA(traits, 60)
    MAService.calcMA(traits, 120)
    return traits[-days:]
