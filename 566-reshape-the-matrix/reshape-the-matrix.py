class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        ret = []
        for _ in range(r):
            ret.append([0] * c)
        curr_row, curr_col = 0, 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                ret[curr_row][curr_col] = mat[i][j]

                if curr_col + 1 >= c:
                    curr_row += 1
                    curr_col = 0
                else:
                    curr_col += 1
        
        return ret