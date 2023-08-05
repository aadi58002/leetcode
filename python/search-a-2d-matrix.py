#!/usr/bin/env python

from typing import List

def binSearch(nums,target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low+high)//2

        if nums[mid] < target:
            low = mid + 1 

        elif nums[mid] > target:
            high = mid - 1 

        else:
            return mid

    return (low+high)//2


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = []
        for i in range(len(matrix)):
            rows.append(matrix[i][0])

        row = binSearch(rows,target)

        col = binSearch(matrix[row],target)
        return matrix[row][col] == target
        
        
    

sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],31))
