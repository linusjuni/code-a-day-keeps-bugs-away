"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        best_profit = 0

        for buy_idx in range(len(prices)):
            for sell_idx in range(buy_idx, len(prices)):
                if prices[sell_idx] - prices[buy_idx] > best_profit:
                    best_profit = prices[sell_idx] - prices[buy_idx]
            
        return best_profit