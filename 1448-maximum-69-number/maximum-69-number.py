class Solution:
    def maximum69Number (self, num: int) -> int:
        # change the first 6 that you see going from left to right

        s = str(num)
        for i in range(len(s)):
            if s[i] == '6':
                return int(s[:i] + "9" + s[i + 1:])
        
        return num