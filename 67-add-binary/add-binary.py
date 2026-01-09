class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        p1 = len(a) - 1
        p2 = len(b) - 1
        res = []

        while p1 >= 0 and p2 >= 0:
            new = int(a[p1]) + int(b[p2]) + carry
            res.append(str(new % 2))
            carry = new // 2

            p1 -= 1
            p2 -= 1
        
        while p1 >= 0:
            new = int(a[p1]) + carry
            res.append(str(new % 2))
            carry = new // 2
            p1 -= 1
        while p2 >= 0:
            new = int(b[p2]) + carry
            res.append(str(new % 2))
            carry = new // 2
            p2 -= 1
        if carry == 1:
            res.append("1")
        res.reverse()
        return "".join(res)
        

