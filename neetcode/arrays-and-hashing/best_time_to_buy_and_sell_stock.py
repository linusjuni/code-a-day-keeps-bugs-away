"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_time = 0
        sell_time = 1
        max_profit = 0

        while sell_time < len(prices):
            if prices[buy_time] < prices[sell_time]:
                profit = prices[sell_time] - prices[buy_time]
                max_profit = max(max_profit, profit)
            else:
                buy_time = sell_time
            sell_time += 1
        return max_profit

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
