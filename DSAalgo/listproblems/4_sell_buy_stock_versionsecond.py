"""
You are given an array of prices where prices[i] is the price of a given stock on an ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

    Input: prices[] = {7, 10, 1, 3, 6, 9, 2}
    Output: 8
    Explanation: Buy for price 1 and sell for price 9.

    Input: prices[] = {7, 6, 4, 3, 1}
    Output: 0
    Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

    Input: prices[] = {1, 3, 6, 9, 11}
    Output: 10
    Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1]


"""
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