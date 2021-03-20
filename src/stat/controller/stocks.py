from .. import stat_bp
from ...db import dboper
from ...tools.response_factory import create_response

@stat_bp.route("/", methods=['GET'])
def getStocks():
    '''
    获取所有的股票代码信息
    '''
    stocks = dboper.getStocks()
    return create_response(stocks)

@stat_bp.route("/<key>", methods=['GET'])
def getStocksByKey(key):
    '''
    获取某支股票的信息

    key:股票代码 或者 名称
    '''
    stocks = dboper.getStocksByKey(key)
    return create_response(stocks)
    
 