class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        m = defaultdict(int)
        m['b'] = 0
        m['a'] = 0
        m['l'] = 0
        m['l'] = 0
        m['o'] = 0
        m['o'] = 0
        m['n'] = 0

        for c in text:
            m[c] += 1

        ret = float('inf')
        for key in m:
            if key in "ban":
                ret = min(ret, m[key])
            elif key in 'lo':
                ret = min(ret, m[key] // 2)
        return ret