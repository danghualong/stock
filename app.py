from src.stat.controller import break_point as bp, stock_filter as sf
from src.stat.view import trends, single_atr_view, single_ma_view
from src.model import Stock

if __name__ == "__main__":
    # Test1
    bp.ShowBreakThroughPoint('300760')

    # Test2
    # result = sf.selectStock(days=10,breakDays=1)
    # print(result)

    # Test3
    # stock = Stock()
    # stock.code = '300760'
    # stock.name="迈瑞医疗"
    # single_ma_view.ShowSingleMA(stock)

    # Test4
    # trends.showCurrentTrends()
