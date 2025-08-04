class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        DIR = 0
        ret = []
        for _ in range(n):
            ret.append([-1] * n)
        ROW, COL = 0, 0
        count = 1

        while count <= n ** 2:
            ret[ROW][COL] = count
            count += 1

            if DIR == 0:
                if COL + 1 >= len(ret[0]) or ret[ROW][COL + 1] != -1:
                    DIR += 1
                    DIR %= 4
                    ROW += 1
                else:
                    COL += 1
            elif DIR == 1:
                if ROW + 1 >= len(ret) or ret[ROW + 1][COL] != -1:
                    DIR += 1
                    DIR %= 4
                    COL -= 1
                else:
                    ROW += 1
            elif DIR == 2:
                if COL - 1 < 0 or ret[ROW][COL - 1] != -1:
                    DIR += 1
                    DIR %= 4
                    ROW -= 1
                else:
                    COL -= 1
            elif DIR == 3:
                if ROW - 1 < 0 or ret[ROW - 1][COL] != -1:
                    DIR += 1
                    DIR %= 4
                    COL += 1
                else:
                    ROW -= 1
        
        return ret