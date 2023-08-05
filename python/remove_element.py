from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        index = 0
        while index < len(nums):
            if nums[index]==val:
                del nums[index]
                count+=1
            else:
                index += 1
        return len(nums)
            
sol = Solution()
num1 = [0,1,2,2,3,0,4,2]
print(sol.removeElement(num1,2))
print(num1)
