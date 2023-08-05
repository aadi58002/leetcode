from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        temp = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k]=temp

sol = Solution()
nums = [1,2,3,4,5,6,7]
sol.rotate(nums,3)
print(nums)
nums = [-1,-100,3,99]
sol.rotate(nums,2)
print(nums)
