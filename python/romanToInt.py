class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        num = val[s[0]]
        for i in range(1,len(s)):
            num += val[s[i]]
            if val[s[i]] > val[s[i-1]]:
                num -= 2*val[s[i-1]]
        return num
                
sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))
