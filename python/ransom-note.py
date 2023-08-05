#!/usr/bin/env python

from typing import List

def countChar(val: str):
    count = {}
    for i in val:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = countChar(ransomNote)
        ma = countChar(magazine)
        for key in list(rn.keys()):
            if not (key in ma) or ma[key] < rn[key]:
                return False
        return True
            
sol = Solution()

print(sol.canConstruct('b','ab'))
