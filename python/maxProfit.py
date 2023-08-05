from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                max_diff += diff
        
        return max_diff

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([7,6,4,3,1]))
print(sol.maxProfit([1,2,3,4,5]))
