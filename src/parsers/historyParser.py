from ..model import Daily
import re
import json


def parse(content):
    pattern = "historySearchHandler\(\[(.*)\]\)"
    pa = re.compile(pattern, re.S)
    arr = pa.findall(content)
    item = arr[0]
    item = json.loads(item)
    code = item["code"]
    series = item["hq"]
    dailys = []
    for d in series:
        daily = Daily()
        daily.date = d[0]
        daily.code = code[3:]
        daily.open = d[1]
        daily.current = d[2]
        daily.last_close = "{:.2f}".format(float(d[2]) - float(d[3]))
        daily.low = d[5]
        daily.high = d[6]
        daily.quantity = str(int(d[7]) * 100)
        daily.amount = "{:.2f}".format(float(d[8]) * 10000)
        daily.turnover = d[9]
        dailys.append(daily)
    return dailys
