class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #00001
        #00011

        x = 1
        while x <= n:
            if x == n:
                return True
            if x > 2 ** 30:
                return False
            
            x = x << 1
        return False

        