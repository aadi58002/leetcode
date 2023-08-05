#!/usr/bin/env python

from typing import List


class Solution(object):
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i,ele in enumerate(citations):
            if ele <= i+1:
                return i+1
        return len(citations)
sol = Solution()
print(sol.hIndex([3,0,6,1,5]))
print(sol.hIndex([1,3,1]))
print(sol.hIndex([4,4,0,0]))
