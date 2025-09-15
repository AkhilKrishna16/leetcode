class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = 0
        ret = float('-inf')
        curr = 0

        while right < len(s):
            if s[right] in "aeiou":
                curr += 1
            
            if right - left + 1 > k:
                if s[left] in "aeiou":
                    curr -= 1
                left += 1
            ret = max(ret, curr)
            right += 1
        return ret