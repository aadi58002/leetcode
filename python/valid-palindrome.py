#!/usr/bin/env python

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for ele in s:
            if ele.isalnum():
                ans += ele.lower()
        print(ans)
        left = 0
        right = len(ans)-1
        while left < right:
            if ans[left] != ans[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
