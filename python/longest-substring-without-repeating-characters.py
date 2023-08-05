#!/usr/bin/env python

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         subseqcount_max = 0
#         for i in range(len(s)):
#             chars = list()
#             count = 0
#             for j in range(i,len(s)):
#                 if s[j] in chars:
#                     break;
#                 else:
#                     chars.append(s[j])
#                 count+=1
#             if subseqcount_max < count:
#                 subseqcount_max = count
#         return subseqcount_max

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_pos = {}
        maxlen = 0
        leng = 0
        prev = 0
        for i in range(len(s)):
            if s[i] in chars_pos:
                prev = max(chars_pos[s[i]] + 1,prev)
            chars_pos[s[i]] = i
            leng = i - prev + 1
            if leng > maxlen:
                maxlen = leng
        return maxlen

sol = Solution()
print(sol.lengthOfLongestSubstring(" "))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("abba"))
print(sol.lengthOfLongestSubstring(" "))
