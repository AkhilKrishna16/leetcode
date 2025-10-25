class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ret = [0, 0]
        for i in range(n.bit_length()):
            if n & 1 == 1:
                print(i % 2)
                if i % 2 == 0:
                    ret[0] += 1
                else:
                    ret[1] += 1
            n >>= 1
        return ret