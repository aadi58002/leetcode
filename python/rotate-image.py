#!/usr/bin/env python

from typing import List


def rotate_layer(matrix: List[List[int]],depth: int):
    length_side = len(matrix) - 2*depth
    if length_side > 1:
        up = matrix[depth][depth:depth+length_side]
        down = matrix[-(depth+1)][depth:depth+length_side]
        left = [matrix[depth+i][depth] for i in range(length_side)]
        right = [matrix[depth+i][-(depth+1)] for i in range(length_side)]

        left.reverse()
        right.reverse()
        matrix[depth][depth:depth+length_side] = left
        matrix[-(depth+1)][depth:depth+length_side] = right
        for i in range(length_side):
            matrix[depth+i][depth] = down[i]

        for i in range(length_side):
            matrix[depth+i][-(depth+1)] = up[i]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            rotate_layer(matrix,i)

sol = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol.rotate(matrix)
print(matrix)
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol.rotate(matrix)
print(matrix)
