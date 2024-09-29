class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while(n != 1 and n not in s):
            s.add(n)
            squared_sum = 0
            while(n > 0):
                squared_sum += (n % 10) ** 2
                n //= 10
            n = squared_sum

        return n == 1