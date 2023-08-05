#!/usr/bin/env python

from typing import List

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[1],dp[2] = 1,2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

        
sol = Solution()
