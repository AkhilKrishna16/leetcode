class Solution:
    def smallestNumber(self, n: int) -> int:
        n += 1
        while True:
            if bin(n).count('1') == 1:
                return n - 1
            n += 1
        return -1