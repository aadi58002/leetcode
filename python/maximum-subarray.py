#!/usr/bin/env python

from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        current_sum = 0
        for ele in nums:
            current_sum += ele
            if max_sum < current_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0

        return max_sum

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.maxSubArray([5,4,-1,7,8]))
print(sol.maxSubArray([-1]))
print(sol.maxSubArray([-2,1]))
