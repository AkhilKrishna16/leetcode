class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        curr = 1
        ret = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ret += min(curr, prev)
                prev = curr
                curr = 1
            else:
                curr += 1
        
        return ret + min(curr, prev)