'''Leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/'''
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

# Solution1
def maxProfit(prices):
    maxp = 0

    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            profit = prices[j]-prices[i]
            if profit > maxp:
                maxp = profit
    return maxp

# T:O(N^2)
# S:O(1)

# Solution2
def maxProfit(prices):
    maxp = 0

    l = 0
    for r in range(1, len(prices)):
        if prices[r] < prices[l]:
            l = r
        maxp = max(maxp, prices[r] - prices[l])
    return maxp

# T: O(N)
# S: O(1)
