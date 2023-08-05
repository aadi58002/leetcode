from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,(len(numbers)-1)
        while (numbers[l]+numbers[r]) != target:
            sum_val = numbers[l]+numbers[r]
            if sum_val < target:
                l += 1
            elif sum_val > target:
                r -= 1
        return [l+1,r+1]
sol = Solution()
print(sol.twoSum([2,7,11,15],9))
print(sol.twoSum([2,3,4],6))
print(sol.twoSum([-1,0,2],-1))
print(sol.twoSum([5,25,75],100))
