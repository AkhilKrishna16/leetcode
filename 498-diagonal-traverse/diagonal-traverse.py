class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ret = [0] * len(mat) * len(mat[0])

        DIR = 1 # 1 is up, -1 is down
        ROW, COL = 0, 0
        count = 0

        while count < len(ret):
            ret[count] = mat[ROW][COL]
            count += 1
            if DIR == 1:
                if COL == len(mat[0]) - 1:
                    ROW += 1
                    DIR = -1
                elif ROW == 0:
                    COL += 1
                    DIR = -1
                else:
                    ROW -= 1
                    COL += 1
            elif DIR == -1:
                if ROW == len(mat) - 1:
                    COL += 1
                    DIR = 1
                elif COL == 0:
                    ROW += 1
                    DIR = 1
                else:
                    ROW += 1
                    COL -= 1
            
        return ret



        