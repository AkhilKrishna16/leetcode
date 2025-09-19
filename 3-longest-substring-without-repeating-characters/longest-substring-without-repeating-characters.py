class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = set()
        res = 0
        left = 0
        
        for right in range(len(s)):
            while s[right] in m and left < right:
                m.remove(s[left])
                left += 1
            
            m.add(s[right])
            res = max(res, right - left + 1)
        
        return res
                