
def getBreakThroughPoint(traits,small,large):
    trait = traits[-2]
    size = len(traits)
    if(size>large):
        return (trait.MA[large] * large * small - traits[-2 - large + 1].close * small - trait.MA[small] * small * large + traits[-2 - small + 1].close * large) / (large - small)
    elif (size > small):
         return (trait.MA[large] * (size-1) *small-trait.MA[small]*small*size+traits[-2-small+1].close*size)/(size-small)
    else:
        return traits[-1].close