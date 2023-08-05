#!/usr/bin/env python

from typing import List

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0: return 1
        bit_x = bin(abs(n))[2:]
        two_power = [x] * (len(bit_x)+1)

        for i in range(1,len(bit_x)+1):
            two_power[i] = two_power[i-1]*two_power[i-1]

        ans = 1
        for i,val in enumerate(reversed(bit_x)):
            if val == '1':
                ans *= two_power[i]

        if n < 0:
            ans = 1/ans
        return ans

    

sol = Solution()
