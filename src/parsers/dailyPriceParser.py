from ..model import Daily


def parse(content):
    d = content.split(",")
    daily = Daily()
    daily.open = d[1]
    daily.last_close = d[2]
    daily.current = d[3]
    daily.high = d[4]
    daily.low = d[5]
    daily.quantity = d[8]
    daily.amount = d[9]
    daily.bid1_amount = d[10]
    daily.bid1 = d[11]
    daily.bid2_amount = d[12]
    daily.bid2 = d[13]
    daily.bid3_amount = d[14]
    daily.bid3 = d[15]
    daily.bid4_amount = d[16]
    daily.bid4 = d[17]
    daily.bid5_amount = d[18]
    daily.bid5 = d[19]
    daily.ask1_amount = d[20]
    daily.ask1 = d[21]
    daily.ask2_amount = d[22]
    daily.ask2 = d[23]
    daily.ask3_amount = d[24]
    daily.ask3 = d[25]
    daily.ask4_amount = d[26]
    daily.ask4 = d[27]
    daily.ask5_amount = d[28]
    daily.ask5 = d[29]
    daily.date = d[30]
    return daily
