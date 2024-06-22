class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0

        while True:
            if n == 4 ** i:
                return True
            elif n < 4 ** i:
                return False

            i += 1

        return False