class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0

        for c in stones:
            if c in jewels:
                res += 1

        return res