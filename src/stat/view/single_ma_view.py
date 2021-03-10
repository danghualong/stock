from ..service import trait_service as TraitService
from . import table

def ShowSingleMA(stock):
    traits = TraitService.getTraits(stock.code)
    table.showMA(traits, stock, True)