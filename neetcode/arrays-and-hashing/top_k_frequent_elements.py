"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        def _create_frequency_buckets(nums: List[int]):
            distinct = {}
            seen = set()
            for num in nums:
                if num not in seen:
                    amount = nums.count(num)
                    if amount not in distinct:
                        distinct[amount] = []
                    distinct[amount].append(num)
                    seen.add(num)
            return distinct

        frequency_buckets = _create_frequency_buckets(nums)
        result = []

        sorted_frequencies = sorted(frequency_buckets.keys(), reverse=True)

        for freq in sorted_frequencies:
            for num in frequency_buckets[freq]:
                if len(result) < k:
                    result.append(num)
                else:
                    return result

        return result
