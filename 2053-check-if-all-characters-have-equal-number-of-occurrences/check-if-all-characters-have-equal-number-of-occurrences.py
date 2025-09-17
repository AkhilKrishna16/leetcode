class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        m = defaultdict(int)

        for c in s:
            m[c] += 1
        
        curr_value = -1

        for key in m:
            if m[key] == curr_value or curr_value == -1:
                curr_value = m[key]
            else:
                return False
        return True