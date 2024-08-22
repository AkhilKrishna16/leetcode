class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for jewel in jewels:
            for stone in stones:
                if stone == jewel:
                    count += 1
        return count