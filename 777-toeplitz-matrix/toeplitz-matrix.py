class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # starting from bottom left, traverse to top right and iterate through the diagonals

        DIR = 3
        ROW, COL = len(matrix) - 1, 0

        while COL < len(matrix[0]):
            # iterate over diagonals
            prev = matrix[ROW][COL]
            ROW_COPY = ROW
            COL_COPY = COL
            ROW_COPY += 1
            COL_COPY += 1
            while ROW_COPY >= 0 and ROW_COPY < len(matrix) and COL_COPY >= 0 and COL_COPY < len(matrix[0]):
                if prev != matrix[ROW_COPY][COL_COPY]:
                    return False
                else:
                    prev = matrix[ROW_COPY][COL_COPY]
                    ROW_COPY += 1
                    COL_COPY += 1
            if DIR == 3:
                if ROW - 1 < 0:
                    DIR = 0
                    COL += 1
                else:
                    ROW -= 1
            else:
                COL += 1

        return True
                     
