

def isTarget(traits,totalDays,breakDays=2,maSlow=5,maFast=10):
    n = len(traits)
    if (totalDays < breakDays):
        return False
    start=n-totalDays
    for i in range(totalDays - breakDays):
        if (traits[start+i].MA[maSlow] > traits[start+i].MA[maFast]):
            return False
    for i in range(breakDays):
        if (traits[n - breakDays + i].MA[maSlow] < traits[n - breakDays + i].MA[maFast]):
            return False
    return True

        
