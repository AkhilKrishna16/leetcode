class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ret = [0] * (len(mat) * len(mat[0]))

        DIR = 1
        ROW, COL = 0, 0
        count = 0

        while ROW >= 0 and ROW < len(mat) and COL >= 0 and COL < len(mat[0]):
            ret[count] = mat[ROW][COL]
            count += 1
            if DIR == 0: # this means we are going down
                if ROW == len(mat) - 1:
                    DIR = 1
                    COL += 1
                elif COL == 0:
                    DIR = 1
                    ROW += 1
                else:
                    ROW += 1
                    COL -= 1
            else: # this means that we are going up
                if COL == len(mat[0]) - 1:
                    DIR = 0
                    ROW += 1
                elif ROW == 0:
                    DIR = 0
                    COL += 1
                else:
                    ROW -= 1
                    COL += 1
                
        
        return ret

        