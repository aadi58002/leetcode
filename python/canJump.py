# Incomplete Problem not solved

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = [False]*len(nums)
        index[-1] = True
        for i in range(len(nums)-1,-1,-1):
            if index[i] == True:
                for j in range(i-1,-1,-1):
                    if nums[j] >= i - j:
                        index[j] = True
        return index[0]

        
sol = Solution()
print(sol.canJump([2,3,1,1,4]))
print(sol.canJump([3,2,1,0,4]))
