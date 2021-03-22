from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from .service import add_stock_service as ass_part
from .service import add_stocks_service as ass_all
from .service import add_history_service as ahs
from .service import add_current_daily_service as acds
from ..logger import currentLogger
import platform,atexit

def init_app(app):
    if platform.system() != 'Windows':
        fcntl = __import__("fcntl")
        f = open('scheduler.lock', 'wb')
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            startJobs(app)
        except:
            pass

        def unlock():
            fcntl.flock(f, fcntl.LOCK_UN)
            f.close()

        atexit.register(unlock)
    else:
        msvcrt = __import__('msvcrt')
        f = open('scheduler.lock', 'wb')
        try:
            msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
            startJobs(app)
        except:
            pass

        def _unlock_file():
            try:
                f.seek(0)
                msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
            except:
                pass

        atexit.register(_unlock_file)

def startJobs(app):
    scheduler = APScheduler(BackgroundScheduler(timezone="Asia/Shanghai"))
    scheduler.init_app(app)
    scheduler.start()
    currentLogger.info("调度任务已开启")

def job1():
    ass_part.addStocks()
    ahs.addHistoryDaily()
    acds.addDaily()