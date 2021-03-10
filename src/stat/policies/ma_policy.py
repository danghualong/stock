

def isTarget(traits,totalDays,breakDays=2,maFastDays=5,maSlowDays=10):
    n = len(traits)
    if (totalDays < breakDays):
        return False
    start=n-totalDays
    for i in range(totalDays - breakDays):
        if (traits[start+i].MA[maFastDays] > traits[start+i].MA[maSlowDays]):
            return False
    for i in range(breakDays):
        if (traits[n - breakDays + i].MA[maFastDays] < traits[n - breakDays + i].MA[maSlowDays]):
            return False
    return True

        
