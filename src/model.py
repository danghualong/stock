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
