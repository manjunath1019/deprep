def stock_multi(sp:list):
    max_profit = 0
    buy = 0
    sell= 1
    n = len(sp)
    print("Len",n)
    while sell < len(sp):
        print(sp[buy],sp[sell],max_profit)
        if sp[sell] < sp[buy]:
            buy= sell
            sell+=1
        else:
            profit= sp[sell]-sp[buy]
            if sell<n-1 and (sp[sell]<sp[sell+1]) :
                sell=sell+1
            else:
                max_profit += profit
                buy=sell+1
                sell+=1
    print(max_profit)
    return max_profit

if __name__ == '__main__':
    stocks  = [3,3,5,0,0,3,1,4]
    result = stock_multi(stocks)
    print(result)