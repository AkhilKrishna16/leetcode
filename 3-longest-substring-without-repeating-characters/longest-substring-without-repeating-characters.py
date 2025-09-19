class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = defaultdict(int)
        res = 0
        left = 0
        
        for right in range(len(s)):
            while s[right] in m and left < right:
                m[s[left]] -= 1
                if m[s[left]] == 0:
                    del m[s[left]]
                left += 1

                
            
            m[s[right]] += 1
            res = max(res, right - left + 1)
        
        return res
                