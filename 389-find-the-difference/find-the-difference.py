class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # return differing values for each string

        for char in t:
            if t.count(char) != s.count(char):
                return char
        
        return ""