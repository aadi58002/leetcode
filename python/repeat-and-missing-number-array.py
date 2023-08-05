#!/usr/bin/env python

from typing import List

class Solution:
    def repeatedNumber(self,A: List[int]) -> List[int]:
        found = [0] * (len(A))
        repeat = -1
        for ele in A:
            if found[ele - 1] == 0:
                found[ele - 1] = 1
            else:
                repeat = ele

        for index,bit in enumerate(found):
            if bit == 0:
                return [repeat,index+1]
        return []
    

sol = Solution()
print(sol.repeatedNumber([3,1,2,5,3]))
