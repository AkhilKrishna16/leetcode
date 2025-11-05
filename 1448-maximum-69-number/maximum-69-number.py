class Solution:
    def maximum69Number (self, num: int) -> int:
        # change the first 6 that you see going from left to right

        # find the first 6 and that position then return num + 3 * 10 ^ (position of first 6)

        pos = -1
        i = 0
        copy = num
        while copy > 0:
            digit = copy % 10
            if digit == 6:
                pos = i
            copy //= 10
            i += 1
        
        if pos == -1:
            return num
        else:
            return num + (3 * 10 ** pos)