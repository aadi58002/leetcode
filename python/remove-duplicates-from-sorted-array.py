from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums)-1:
            if nums[index]==nums[index+1]:
                del nums[index+1]
            else:
                index += 1
        return len(nums)
            

sol = Solution()
print(sol.removeDuplicates([1,1,2]))
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
