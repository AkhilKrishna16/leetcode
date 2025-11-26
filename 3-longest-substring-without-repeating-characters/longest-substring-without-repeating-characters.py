class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        m = set()
        ret = 0

        for right in range(len(s)):
            curr = s[right]

            while curr in m:
                m.remove(s[left])
                left+= 1

            m.add(s[right])
            ret = max(ret, right - left + 1)
        
        return ret

                