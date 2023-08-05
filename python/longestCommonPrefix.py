from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for ele in strs:
            while not ele.startswith(common):
                common = common[:-1]
        return common

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
