"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if (i > 0) and (a == nums[i - 1]):
                continue

            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                summation = a + b + c

                if summation > 0:
                    right -= 1

                elif summation < 0:
                    left += 1

                else:
                    result.append([a, b, c])
                    left += 1

                    while (nums[left] == nums[left - 1]) and (left < right):
                        left += 1

        return result

