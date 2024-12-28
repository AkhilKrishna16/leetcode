class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0

        while x != 0 or y != 0:
            count += (x & 1) ^ (y & 1)
            x = x >> 1
            y = y >> 1
        
        return count