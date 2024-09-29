class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        m = {}

        for i in range(len(s)):
            if s[i] not in m and t[i] not in m.values():
                m[s[i]] = t[i]
            elif s[i] not in m or m[s[i]] != t[i]:
                return False        
        return True