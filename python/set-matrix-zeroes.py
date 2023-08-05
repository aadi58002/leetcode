#!/usr/bin/env python
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        no_row = len(matrix)
        no_col = len(matrix[no_row-1])

        mark_row = set()
        mark_col = set()
        for row in range(no_row):
            for col in range(no_col):
                if matrix[row][col] == 0:
                    mark_row.add(row)
                    mark_col.add(col)

        for row in mark_row:
            for i in range(no_col):
                matrix[row][i] = 0

        for col in mark_col:
            for i in range(no_row):
                matrix[i][col] = 0

sol = Solution();
mat = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(mat)
print(mat)
