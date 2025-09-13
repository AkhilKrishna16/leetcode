class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = 0
        a = [0]

        for g in gain:
            curr = g + a[-1]
            a.append(curr)
            m = max(curr, m)
        
        return m
