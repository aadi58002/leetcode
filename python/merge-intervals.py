#!/usr/bin/env python

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:    
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        
        ans = []

        prev = intervals[0]
        for ele in intervals[1:]:
            if prev[1] >= ele[0]:
                prev[1] = max(ele[1],prev[1])
            else:
                ans.append(prev)
                prev = ele

        ans.append(prev)
        return ans
        
        

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[1,4],[4,5]]))
