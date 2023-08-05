# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = ' ' + s
#         ans = ""
#         index = len(s)-1
#         leng = 0
#         for i in range(len(s)-1,-1,-1):
#             if s[i] == ' ':
#                 if leng != 0:
#                     ans += s[index-leng+1:index+1] + ' '
#                 index = i-1
#                 leng = 0
#             else:
#                 leng += 1
#         return ans[:-1]

class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        for ele in reversed(s.split(" ")):
            if ele != '':
                ans += ele + ' '
        return ans[:-1]

sol = Solution()
print(sol.reverseWords("the sky is blue"))
print(sol.reverseWords("  hello world  "))
