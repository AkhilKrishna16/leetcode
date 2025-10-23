class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

        # we check n > 0

        # we check that the number is a power of two. this means that we only get values 
        # with a singular bit set since powers of 4 can only have a singular bit set
        # this goes with powers of 2,4,8,etc. because our next condition is not enough
        # even though it truly finds the ones with bits in an odd position

        # we perform and operation with n and 010101010101... to find if there are  
        # bits set in the odd position. because of the previous condition, we would
        # only be checking numbers with one bit set