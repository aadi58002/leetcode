#!/usr/bin/env python

from typing import List

## Part 1
# class Solution:
#     def majorityElement(self, nums: List[int]):
#         count = dict()
#         for ele in nums:
#             if ele in count:
#                 count[ele] += 1
#             else:
#                 count[ele] = 1
#             if count[ele] >= len(nums)/2:
#                 return ele

## Part 2
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = dict()
        for ele in nums:
            if ele in count:
                count[ele] += 1
            else:
                count[ele] = 1
            
        ans = []
        for key,ele in count.items():
            if ele >= len(nums)/3:
                ans.append(key)
        return ans

sol = Solution()
print(sol.majorityElement([3,2,3]));

print(sol.majorityElement([2,2,1,1,1,2,2]));
