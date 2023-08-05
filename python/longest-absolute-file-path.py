#!/usr/bin/env python

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        dirs = input.split('\n')
        stack,max_len = [0],0
        for path in dirs:
            p = path.split('\t')
            level = len(p)
            name = p[-1]
            while len(stack) > level:
                stack.pop()
            if '.' in name:
                max_len = max(max_len,len(name)+stack[-1])
            else:
                stack.append(stack[-1]+len(name)+1)
        return max_len

sol = Solution()
print(sol.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
print(sol.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
