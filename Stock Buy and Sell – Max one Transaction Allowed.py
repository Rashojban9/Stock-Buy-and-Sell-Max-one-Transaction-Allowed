def max_profit(price):
    n=len(price)
    res=0
    for i in range(n-1):
        for j in range(i+1,n):
            res=max(res,price[j]-price[i])
    return res
price=[7,10,1,3,6,9,2]
print(max_profit(price))
