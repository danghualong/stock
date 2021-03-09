

def isTarget(traits,breakDays=2,maSlow=5,maFast=10):
    n = len(traits)
    if (n < breakDays):
        return False
    for i in range(n - breakDays):
        if (traits[i].MA[maSlow] > traits[i].MA[maFast]):
            return False
    for i in range(breakDays):
        if (traits[n - breakDays + i].MA[maSlow] < traits[n - breakDays + i].MA[maFast]):
            return False
    return True

        
