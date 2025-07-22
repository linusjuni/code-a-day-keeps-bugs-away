"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        length_groups = {}
        anagram_groups = {}

        for string in strs:
            length = len(string)
            if length not in length_groups:
                length_groups[length] = []
            length_groups[length].append(string)

        for length in length_groups:
            strings_of_this_length = length_groups[length]

            for string in strings_of_this_length:
                sorted_key = "".join(sorted(string))
                if sorted_key not in anagram_groups:
                    anagram_groups[sorted_key] = []
                anagram_groups[sorted_key].append(string)

        return list(anagram_groups.values())
