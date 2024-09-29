class Solution:
    def addDigits(self, num: int) -> int:
        # while loop -> digits > 1 -> total += digit % 10; digit /= 10
        total = num
        while num >= 10:
            total = 0
            while(num > 0):
                total += num % 10
                num //= 10
    
            num = total

        return total
