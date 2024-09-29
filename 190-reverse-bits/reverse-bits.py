class Solution:
    def reverseBits(self, n: int) -> int:
        # 010110 -> 011010
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        
        return result