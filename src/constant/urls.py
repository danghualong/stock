DAILY_PRICE_URL = 'http://hq.sinajs.cn/list={0}'  # sz表示深市，sh表示上市
HISTORY_PRICE_URL = 'https://q.stock.sohu.com/hisHq?code=cn_{0}&start={1}&end={2}&stat=0&order=A&period=d&callback=historySearchHandler&rt=jsonp'
# appkey从个人管理后台获取：https://www.jisuapi.com/api/stock/
JISU_STOCK_URL='https://api.jisuapi.com/stock/list?classid=1&pagenum={0}&pagesize=40&appkey=9c9d121ac353b5c1'