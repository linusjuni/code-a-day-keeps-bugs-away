"""
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
"""

from typing import List


class Solution:

    @staticmethod
    def _perform_operation(first, operator, second):
            first = int(first)
            second = int(second)

            if operator == '+':
                return first + second
            elif operator == '-':
                return first - second
            elif operator == '*':
                return first * second
            elif operator == '/':
                return int(first / second)
            else:
                raise ValueError
    
    def evalRPN(self, tokens: List[str]) -> int:

        operators = ['+', '-', '*', '/']
        stack = []

        for i, token in enumerate(tokens):
            
            if token not in operators:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                result = self._perform_operation(first, token, second)
                stack.append(result)

        print(stack[0])
        return stack[0]
                
sol = Solution()
sol.evalRPN(["4","13","5","/","+"])