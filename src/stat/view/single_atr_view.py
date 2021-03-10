from ..service import trait_service as TraitService
from . import table

def ShowSingleATR(stock):
    traits = TraitService.getTraits(stock.code)
    table.showATR(traits, stock, True)