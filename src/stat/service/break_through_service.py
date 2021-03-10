
def getBreakThroughPoint(traits, maFastDays, maSlowDays):
    '''
    计算当前价格要变化到什么值能形成突破

    traits:汇总特征数据集合
    maFastDays:快线天数
    maSlowDays:慢线天数
    '''
    trait = traits[-2]
    size = len(traits)
    if(size>maSlowDays):
        return (trait.MA[maSlowDays] * maSlowDays * maFastDays - traits[-2 - maSlowDays + 1].close * maFastDays - trait.MA[maFastDays] * maFastDays * maSlowDays + traits[-2 - maFastDays + 1].close * maSlowDays) / (maSlowDays - maFastDays)
    elif (size > maFastDays):
         return (trait.MA[maSlowDays] * (size-1) *maFastDays-trait.MA[maFastDays]*maFastDays*size+traits[-2-maFastDays+1].close*size)/(size-maFastDays)
    else:
        return traits[-1].close