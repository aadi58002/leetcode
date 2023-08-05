#!/usr/bin/env python

class Solution(object):
    def strStr(self, haystack: str, needle: str):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # return haystack.find(needle)
        for start in range(len(haystack)-len(needle)+1):
            if haystack[start:start+len(needle)] == needle:
                return start
        return -1            
sol = Solution()
print(sol.strStr("sadbutsad", "sad"))
print(sol.strStr("leetcode", "leeto"))
print(sol.strStr("hello", "ll"))


