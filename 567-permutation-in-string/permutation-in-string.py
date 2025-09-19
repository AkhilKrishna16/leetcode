class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        ref = defaultdict(int)
        res = defaultdict(int)
        for i in range(len(s1)):
            ref[s1[i]] += 1
            res[s2[i]] += 1
        if res == ref:
            return True
        left = 0
        for right in range(len(s1), len(s2)):
            res[s2[right]] += 1
            res[s2[left]] -= 1
            
            
            if res[s2[left]] == 0:
                del res[s2[left]]
            left += 1
            
            if res == ref:
                return True
        
        return False
        
        return False