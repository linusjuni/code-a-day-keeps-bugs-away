"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:
1. Every open bracket is closed by the same type of close bracket.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        if len(s) % 2 == 1:
            return False

        def _assert_opening_matches_closes(last: str, p: str) -> bool:
            if last == "(":
                return True if p == ")" else False
            elif last == "{":
                return True if p == "}" else False
            elif last == "[":
                return True if p == "]" else False
            else:
                return False

        openings = []
        closings = []

        opening_parenthesis = ["(", "{", "["]
        closing_parenthesis = [")", "}", "]"]

        for i, p in enumerate(s):
            if p in opening_parenthesis:
                openings.append(p)

                if i == len(s) - 1:
                    return False

                continue

            if p in closing_parenthesis:
                if len(openings) == 0:
                    return False
                last = openings.pop()
                if _assert_opening_matches_closes(last, p):
                    continue
                return False

        return len(openings) == 0
