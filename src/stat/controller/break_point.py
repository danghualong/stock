from ..service import trait_service as TraitService,break_through_service as btService

def ShowBreakThroughPoint(code):
    traits = TraitService.getTraits(code)
    # 估计当天短线突破长线的当前价格
    btp = btService.getBreakThroughPoint(traits, 5, 10)
    print("ma5:{0},ma10:{1}".format(round(traits[-1].MA[5],3),round(traits[-1].MA[10],3)))
    print("BreakThroughPoint:{0}".format(round(btp,3)))