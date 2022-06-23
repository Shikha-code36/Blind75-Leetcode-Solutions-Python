'''Leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/'''

#Solution1
def maxProfit(prices):
    maxp= 0

    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            profit = prices[j]-prices[i]
            if profit>maxp:
                maxp=profit
    return maxp

#T:O(N^2)
#S:O(1)

#Solution2
def maxProfit(prices):
    maxp= 0

    l = 0
    for r in range(1, len(prices)):
        if prices[r] < prices[l]:
                l = r
        maxp = max(maxp, prices[r] - prices[l])
    return maxp

# T: O(N)
# S: O(1)
