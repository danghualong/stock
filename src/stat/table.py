import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

def showMAAndATR(traits, stock):
    plt.subplot(2, 1, 1)
    showMA(traits, stock)
    plt.subplot(2, 1, 2)
    showATR(traits, stock)
    plt.show()

def showATR(traits, stock, autoShow=False):  
    y1 = list(map(lambda p: p.ATR[10],traits))
    y2 = list(map(lambda p: p.getTrueRange(),traits))
    plt.plot(range(len(y1)), y1,marker='o',markersize=3,label='ATR10')
    plt.plot(range(len(y1)), y2, marker='*', markersize=3, label='TR')
    plt.legend()
    if (autoShow):
        plt.title("{0}({1})".format(stock.name,stock.code))
        plt.show()

def showMA(traits,stock,autoShow=False):
    plt.title("{0}({1})".format(stock.name,stock.code))
    y1 = list(map(lambda p: p.MA[5],traits))
    y2 = list(map(lambda p: p.MA[10],traits))
    y3 = list(map(lambda p: p.MA[20],traits))
    y4 = list(map(lambda p: p.MA[30],traits))
    y5 = list(map(lambda p: p.MA[60],traits))
    y6 = list(map(lambda p: p.MA[120],traits))
    plt.plot(range(len(y1)), y1,marker='o',markersize=3,label='MA05')
    plt.plot(range(len(y1)), y2,marker='*',markersize=3,label='MA10')
    plt.plot(range(len(y1)), y3, marker='^', markersize=3, label='MA20')
    plt.legend()
    # plt.plot(range(len(y1)), y4)
    # plt.plot(range(len(y1)), y5)
    # plt.plot(range(len(y1)), y6)
    if (autoShow):
        plt.show()