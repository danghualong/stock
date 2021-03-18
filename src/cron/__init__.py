from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from .service import add_stock_service as ass_part
from .service import add_stocks_service as ass_all
from .service import add_history_service as ahs
from .service import add_current_daily_service as acds

def init_app(app):
    scheduler = APScheduler(BackgroundScheduler(timezone="Asia/Shanghai"))
    scheduler.init_app(app)
    scheduler.start()

def job1():
    ass_part.addStocks()
    ahs.addHistoryDaily()
    acds.addDaily()