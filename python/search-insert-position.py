#!/usr/bin/env python

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-1
        while low < high:
            middle = int((low + high)/2)
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1

        if nums[high] < target:
            return high + 1
        else:
            return high

sol = Solution()
print(sol.searchInsert([1,3,5,6],5))
print(sol.searchInsert([1,3,5,6],2))
print(sol.searchInsert([1,3,5,6],7))
print(sol.searchInsert([1,3,5,6],0))
print(sol.searchInsert([1,3],0))
