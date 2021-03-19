import time


class Synchronizable(object):
    update_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


class Stock(Synchronizable):
    code = ''
    name = ''
    prefix = 'sh'

class Daily(Synchronizable):
    code = ""
    date = ""
    open = ""
    last_close = ""
    current = ""
    high = ""
    low = ""
    quantity = ""
    amount = ""
    bid1 = ""
    bid1_amount = ""
    bid2 = ""
    bid2_amount = ""
    bid3 = ""
    bid3_amount = ""
    bid4 = ""
    bid4_amount = ""
    bid5 = ""
    bid5_amount = ""
    ask1 = ""
    ask1_amount = ""
    ask2 = ""
    ask2_amount = ""
    ask3 = ""
    ask3_amount = ""
    ask4 = ""
    ask4_amount = ""
    ask5 = ""
    ask5_amount = ""
    turnover = ""

class Trait(object):
    date = ""
    # # 移动平均线
    # MA = {}
    # # 平均真实波动幅度
    # ATR={}
    close = 0.0
    high = 0.0
    last_close=0.0
    low = 0.0
    open = 0.0
    quantity = 0.0
    amount = 0.0

    def __init__(self):
        # 移动平均线
        self.MA = {}
        # 平均真实波动幅度
        self.ATR = {}
    
    # 获取当日真实波动幅度
    def getTrueRange(self):
        return max(self.high - self.low, abs(self.high - self.last_close), abs(self.low - self.last_close))

    def __str__(self):
        return "----{8}----,atr10:{0},atr20:{1},ma5:{2},ma10:{3},ma20:{4},ma30:{5},ma60:{6},ma120:{7}".format(round(self.ATR[10], 3),
            round(self.ATR[20], 3),
            round(self.MA[5], 3),
            round(self.MA[10], 3),
            round(self.MA[20], 3),
            round(self.MA[30], 3),
            round(self.MA[60], 3),
            round(self.MA[120], 3),
            self.date)
        
