class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ref = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            curr = Counter(s2[i:i + len(s1)])
            if curr == ref:
                return True
        
        return False