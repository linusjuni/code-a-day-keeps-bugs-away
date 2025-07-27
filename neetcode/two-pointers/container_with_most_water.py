"""
You are given an integer array heights where heights[i] represents the height of the i'th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
"""

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water_amount = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            water_amount = width * height

            max_water_amount = max(max_water_amount, water_amount)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_water_amount
