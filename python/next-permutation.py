#!/usr/bin/env python

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index_replace = -1
        for i in reversed(range(1,len(nums))):
            if nums[i-1] < nums[i]:
                index_replace = i - 1
                break

        swap_min_index = -1
        for i in reversed(range(len(nums))):
            if nums[i] > nums[index_replace]:
                swap_min_index = i
                break

        nums[index_replace],nums[swap_min_index] = nums[swap_min_index],nums[index_replace]
        nums[index_replace+1:] = sorted(nums[index_replace+1:])

sol = Solution()
nums = [1,2,3]
nums = [3,2,1]
nums = [1,1,5]
nums = [1,3,2]
sol.nextPermutation(nums)
print(nums)
