"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
"""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        all_strings = ""
        lengths = []
        for s in strs:
            lengths.append(len(s))
            all_strings += s

        lengths_str = ""
        for length in lengths:
            lengths_str += str(length) + ","

        return all_strings + " | " + lengths_str[:-1]

    def decode(self, s: str) -> List[str]:

        if s == "":
            return []

        parts = s.split(" | ", 1)
        all_strings = parts[0]
        lengths_string = parts[1]

        lengths = lengths_string.split(",")

        decoded = []
        i = 0

        for length in lengths:

            to_append = all_strings[i : int(length) + i]
            i += int(length)
            decoded.append(to_append)

        return decoded
