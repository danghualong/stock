
def calcATR(traits, N=20):
    '''
    计算N日平均波动幅度

    traits:汇总特征数据集合
    N:均值的天数
    '''
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
