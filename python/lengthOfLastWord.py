class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        leng = 0
        while s[-1]==' ':
            s = s[:-1]
        for c in s:
            if c == ' ':
                leng=0
            else:
                leng+=1
        return leng

sol = Solution()
print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("luffy is still joybo"))
