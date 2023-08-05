#!/usr/bin/env python

from typing import List
import math

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return [[math.comb(i,j) for j in range(i+1)] for i in range(numRows)]

sol = Solution()

print(sol.generate(5))
