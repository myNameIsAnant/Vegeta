"""
LeetCode: 121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""

from typing import List


def maxProfit(prices: List[int]) -> int:
    max_profit = cp = 0
    for i in range(len(prices)):
        if i == 0 or (prices[i] < cp):
            cp = prices[i]
        else:
            max_profit = max(max_profit, (prices[i] - cp))
    return max_profit


pricelist = [7, 1, 5, 3, 6, 4]
print(maxProfit(pricelist))
