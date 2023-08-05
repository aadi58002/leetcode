#!/usr/bin/env python

from typing import List

def comb(n,r):
    if r>n: n,r = r,n
    top = 1
    for i in range(n-r+1,n+1):
        top *= i
    btm = 1
    for i in range(1,r+1):
        btm *= i

    return top/btm
        

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return comb(m+n-2,m-1)

sol = Solution()

print(sol.uniquePaths(3,7))
