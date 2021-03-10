from src.cron.service import add_stock_service as AddStockService, add_stocks_service as AddStocksService, add_history_service as ahs, add_current_daily_service as acds

if __name__=="__main__":
    AddStockService.addStocks()
    ahs.addHistoryDaily()
    acds.addDaily()
