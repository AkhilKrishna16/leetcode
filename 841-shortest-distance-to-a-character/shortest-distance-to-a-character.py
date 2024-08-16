class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []
        pos = []

        for i in range(len(s)):
            if c == s[i]:
                pos.append(i)
        
        print(pos)
        
        for i in range(len(s)):
            m = float('inf') 
            for val in pos:
                m = min(m, abs(val - i))
            
            res.append(m)

        return res