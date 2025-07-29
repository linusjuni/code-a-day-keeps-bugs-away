"""
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total_water_amount = 0

        for i, h in enumerate(height):

            if (i == 0) or (i == len(height) - 1):
                continue

            left = i - 1
            right = i + 1

            water_at_i = max(0, min(height[left], height[right]) - h)
            print(i, water_at_i)
            total_water_amount += water_at_i

        return total_water_amount


height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
sol = Solution()
sol.trap(height)
