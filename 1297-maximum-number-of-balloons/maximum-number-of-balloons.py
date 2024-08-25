class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        m = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for c in text:
            if c in ('b', 'a', 'l', 'o', 'n'):
                if c in m:
                    m[c] += 1
                else:
                    m[c] = 1
        

        mi = float('inf')

        for key in m:
            if key == 'l' or key == 'o':
                val = m[key] // 2
            else:
                val = m[key]
            
            mi = min(mi, val)
        return mi