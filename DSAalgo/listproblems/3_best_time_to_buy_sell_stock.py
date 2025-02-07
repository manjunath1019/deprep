def stock_max_profit(sp:list):
    max_profit=0
    buy=sp[0]
    for sell in range(1,len(sp)):
        profit = sp[sell]-buy
        print(buy,sp[sell],profit,max_profit)
        max_profit = max(max_profit,profit)
        buy = min(sp[sell],buy)
    return max_profit





if __name__ == '__main__':
    #stockprice = [1,2,3,4,5,10]
    stockprice = [3,3,5,0,0,3,1,4]
    #stockprice =[1,2,7,4]
    profit= stock_max_profit(stockprice)
    print(profit)
    print("-------------------------------------")
    stock_multi(sp=stockprice)
