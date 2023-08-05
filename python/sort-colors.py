#!/usr/bin/env python

from typing import List

def merge_partitions(arr1: List[int],arr2: List[int]) -> List[int]:
    i1 = 0
    i2 = 0
    ans = []
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] < arr2[i2]:
           ans.append(arr1[i1])
           i1 += 1
        else:
           ans.append(arr2[i2])
           i2 += 1
    while i1 < len(arr1):
        ans.append(arr1[i1])
        i1 += 1
    while i2 < len(arr2):
        ans.append(arr2[i2])
        i2 += 1

    return ans

def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) == 1:
        return nums
    else:
        return merge_partitions(merge_sort(nums[:len(nums)//2]),merge_sort(nums[len(nums)//2:]))

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums[:] = merge_sort(nums)
        
sol = Solution()
nums = [2,0,2,1,1,0]
sol.sortColors(nums)
print(nums)

