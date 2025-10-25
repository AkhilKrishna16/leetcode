class Solution:
    def binaryGap(self, n: int) -> int:
        most_recent = None
        ret = float('-inf')
        for i in range(n.bit_length()):
            if n & 1 == 1:
                print(f"{most_recent} - {i}")
                if most_recent != None:
                    ret = max(ret, abs(i - most_recent))   
                most_recent = i
            
            n >>= 1
        return 0 if ret == float('-inf') else ret