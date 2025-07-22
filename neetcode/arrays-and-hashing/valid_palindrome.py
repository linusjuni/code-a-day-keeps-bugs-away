"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_to_check = "".join(char.lower() for char in s if char.isalnum())

        if string_to_check == string_to_check[::-1]:
            return True
        return False
