

def calcMA(traits, N=5):
    '''
    计算N日均线值

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
            total += trait.close
            trait.MA[N] = total / (fastIndex + 1)
        else:
            total = total - traits[slowIndex].close + trait.close
            trait.MA[N]=total/N
            slowIndex += 1
