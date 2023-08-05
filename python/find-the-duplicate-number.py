#!/usr/bin/env python

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        found = [0] * (len(nums))
        for ele in nums:
            if found[ele - 1] == 0:
                found[ele - 1] = 1
            else:
                return ele

sol = Solution()
