class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = (1 << n.bit_length()) - 1
        return n ^ mask if n != 0 else 1