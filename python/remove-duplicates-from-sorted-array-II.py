from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index,repeat = 0,False
        while index < len(nums)-1:
            if nums[index]==nums[index+1]:
                if repeat:
                    del nums[index+1]
                else:
                    index+=1
                    repeat=True 
            else:
                index += 1
                repeat=False 
        return len(nums)

sol = Solution()
# num = [1,1,1,2,2,3]
num = [0,0,1,1,1,1,2,3,3]
print(sol.removeDuplicates(num))
print(num)

