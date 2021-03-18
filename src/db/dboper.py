import sqlite3
import os
from ..model import Daily, Stock
from ..settings import configs
from ..logger import currentLogger


DB_NAME = configs[os.getenv("FLASK_ENV", "development")].SQLALCHEMY_DATABASE_URI

def insertStock(stock):
    try:
        conn = sqlite3.connect(DB_NAME)
        # print("insertStock connect db successfully")
        cur = conn.cursor()
        cur.execute(
            'insert or ignore into stock(code,name,prefix,update_at) values(?,?,?,?)',
            (
                stock.code,
                stock.name,
                stock.prefix,
                stock.update_at,
            ))
        conn.commit()
    except Exception as e:
        currentLogger.error("%s",e)
    finally:
        if cur!=None:
            cur.close()
        if conn!=None:
            conn.close()

def getStocks():
    result = []
    try:
        conn = sqlite3.connect(DB_NAME)
        # print("getStocks connect db successfully")
        cur = conn.cursor()
        cur.execute('select * from stock where type<9')
        items = cur.fetchall()
        for item in items:
            stock = Stock()
            stock.code = item[0]
            stock.name = item[1]
            stock.prefix = item[2]
            result.append(stock)
    except Exception as e:
        currentLogger.error("%s",e)
    finally:
        if cur!=None:
            cur.close()
        if conn!=None:
            conn.close()
    return result

def insertDaily(daily, replace=False):
    try:
        conn = sqlite3.connect(DB_NAME)
        # print("insertDaily connect db successfully")
        cur = conn.cursor()
        cur.execute(
            '''insert or {0} into daily(
                code,date,open,last_close,current,high,low,quantity,amount,
                bid1,bid2,bid3,bid4,bid5,ask1,ask2,ask3,ask4,ask5,
            bid1_amount,bid2_amount,bid3_amount,bid4_amount,bid5_amount,
            ask1_amount,ask2_amount,ask3_amount,ask4_amount,ask5_amount,
            turnover,update_at) values
            (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''.
            format('replace' if replace else 'ignore'), (
                daily.code,
                daily.date,
                daily.open,
                daily.last_close,
                daily.current,
                daily.high,
                daily.low,
                daily.quantity,
                daily.amount,
                daily.bid1,
                daily.bid2,
                daily.bid3,
                daily.bid4,
                daily.bid5,
                daily.ask1,
                daily.ask2,
                daily.ask3,
                daily.ask4,
                daily.ask5,
                daily.bid1_amount,
                daily.bid2_amount,
                daily.bid3_amount,
                daily.bid4_amount,
                daily.bid5_amount,
                daily.ask1_amount,
                daily.ask2_amount,
                daily.ask3_amount,
                daily.ask4_amount,
                daily.ask5_amount,
                daily.turnover,
                daily.update_at,
            ))
        conn.commit()
    except Exception as e:
        currentLogger.error("%s",e)
    finally:
        if cur!=None:
            cur.close()
        if conn!=None:
            conn.close()

def getDailys(code,N):
    result = []
    try:
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute('select * from daily where code=? order by date desc limit ?',(code,N,))
        items = cur.fetchall()
        for item in items:
            daily = Daily()
            daily.code = item[0]
            daily.date = item[1]
            daily.open = item[2]
            daily.last_close = item[3]
            daily.current = item[4]
            daily.high = item[5]
            daily.low = item[6]
            daily.quantity = item[7]
            daily.amount = item[8]
            daily.bid1 = item[9]
            daily.bid1_amount = item[10]
            daily.bid2 = item[11]
            daily.bid2_amount = item[12]
            daily.bid3 = item[13]
            daily.bid3_amount = item[14]
            daily.bid4 = item[15]
            daily.bid4_amount = item[16]
            daily.bid5 = item[17]
            daily.bid5_amount = item[18]
            daily.ask1 = item[19]
            daily.ask1_amount = item[20]
            daily.ask2 = item[21]
            daily.ask2_amount = item[22]
            daily.ask3 = item[23]
            daily.ask3_amount = item[24]
            daily.ask4 = item[25]
            daily.ask4_amount = item[26]
            daily.ask5 = item[27]
            daily.ask5_amount = item[28]
            daily.turnover = item[30]
            result.append(daily)
    except Exception as e:
        currentLogger.error("%s",e)
    finally:
        if cur!=None:
            cur.close()
        if conn!=None:
            conn.close()
    return result[::-1]

if __name__ == "__main__":

    from model import Stock, Daily

    stock = Stock()
    stock.name = "美的集团"
    stock.code = "000333"
    stock.prefix = "sz"
    insertStock(stock)

    daily = Daily()
    daily.code = "000333"
    daily.date = "2021-02-10"
    daily.open = "102.9"
    daily.last_close = "101.7"
    daily.current = "107.2"
    daily.high = "108"
    daily.low = "101.5"
    daily.quantity = "8654778686"
    daily.amount = "1545678968498786.01"
    daily.bid1 = "107.1"
    daily.bid2 = "107.0"
    daily.bid3 = "106.9"
    daily.bid4 = "106.7"
    daily.bid5 = "106.0"
    daily.bid1_amount = "3047"
    daily.bid2_amount = "3048"
    daily.bid3_amount = "3046"
    daily.bid4_amount = "3045"
    daily.bid5_amount = "3044"
    daily.ask1 = "107.2"
    daily.ask2 = "107.3"
    daily.ask3 = "107.4"
    daily.ask4 = "107.5"
    daily.ask5 = "107.6"
    daily.ask1_amount = "5041"
    daily.ask2_amount = "5042"
    daily.ask3_amount = "5043"
    daily.ask4_amount = "5044"
    daily.ask5_amount = "5045"
    insertDaily(daily)
