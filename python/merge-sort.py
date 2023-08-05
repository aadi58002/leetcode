from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        while len(nums1) > m:
            nums1.pop()
        l1,l2 = 0,0
        while l1 < len(nums1) and l2 < n:
            if nums1[l1] >= nums2[l2]:
                nums1.insert(l1,nums2[l2])
                l2 += 1
            l1 += 1
        while l2 != n:
            nums1.append(nums2[l2])
            l2+=1
        
            
sol = Solution()
num1 = [4,0,0,0,0,0]
sol.merge(num1,1,[1,2,3,5,6],5)
print(num1)
