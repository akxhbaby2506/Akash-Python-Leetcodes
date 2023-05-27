
def maxProfit(prices):
    
    minimum = min(prices)
    print("least cost",minimum)
    if minimum == prices[len(prices)-1]:
        print(0)

    for i in range(len(prices)):

        if prices[i] == minimum:
            print("minimum cost day: ",i)

            for j in range(len(prices)-1, i+2, -1):
                if prices[j]>prices[j-1]:
                    print("profitable price is: ",prices[j]," on day: ",j)
                    print("PROFIT is: ",prices[j]-minimum)




maxProfit([7,1,4,5,6,2])
print()
maxProfit([5,8,3,4,9,1])

def maxProf(prices):
    res = 0
    low = prices[0]
    for price in prices:
        if price<low:
            low = price
        res = max(res,price-low)
    return res
print(maxProf([7,1,4,5,6,2]))