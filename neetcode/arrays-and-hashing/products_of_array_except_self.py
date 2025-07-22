"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == 0:
                    if i != j:
                        product = product * nums[j]
                else:
                    product = product * nums[j]
            if nums[i] != 0:
                output.append(product // nums[i])
            else:
                output.append(product)
            product = 1
        return output
