#!/usr/bin/env python

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        ans,start,end,sum_subarray = [0,0],0,0,0
        while end <= len(nums):
            if sum_subarray >= target:
                current_diff = ans[1] - ans[0]
                if current_diff > (end - start) or current_diff == 0:
                    ans = [start,end]
                sum_subarray -= nums[start]
                start += 1
            elif end != len(nums):
                sum_subarray += nums[end]
                end += 1
            else:
                break
        return ans[1]-ans[0]

sol = Solution()
print(sol.minSubArrayLen(7,[2,3,1,2,4,3]));
print(sol.minSubArrayLen(4,[1,4,4]));
print(sol.minSubArrayLen(11,[1,4,4]));
