"""
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        valid_numbers = {"1","2","3","4","5","6","7","8","9", "."}
        
        def _check_rows(board):
            for row in board:
                seen = set()
                for j in row:
                    if j not in valid_numbers:
                        return False
                    if j == '.': 
                        continue
                    if j in seen:
                        return False
                    seen.add(j)
            return True
        
        def _check_columns(board):
            for i in range(len(board)):
                seen = set()
                for row in board:
                    column_element = row[i]
                    if column_element not in valid_numbers:
                        return False
                    if column_element == '.':
                        continue
                    if column_element in seen:
                        return False
                    seen.add(column_element)
            return True
        
        def _check_boxes(board):
            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    seen = set()
                    for i in range(3):
                        for j in range(3):
                            val = board[box_row + i][box_col + j]
                            if val not in valid_numbers:
                                return False
                            if val == '.':
                                continue
                            if val in seen:
                                return False
                            seen.add(val)
            return True  
                        
        if _check_rows(board) and _check_columns(board) and _check_boxes(board):
            return True
        else:
            return False