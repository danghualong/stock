from ..service import trait_service as TraitService, break_through_service as btService
from .. import stat_bp
from flask import jsonify


@stat_bp.route("/breakpoints/<code>", methods=['GET','POST'])
def ShowBreakThroughPoint(code):
    traits = TraitService.getTraits(code)
    # 估计当天短线突破长线的当前价格
    btp = btService.getBreakThroughPoint(traits, 5, 10)
    lastTrait = traits[-1]
    print(lastTrait)
    return jsonify({
        "code": code,
        "date": lastTrait.date,
        "ma5": round(lastTrait.MA[5], 3),
        "ma10": round(lastTrait.MA[10], 3),
        "target":round(btp,3)
        })
