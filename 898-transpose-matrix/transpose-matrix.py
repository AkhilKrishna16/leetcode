class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ret = []
        for _ in range(len(matrix[0])):
            ret.append([0] * len(matrix))
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ret[j][i] = matrix[i][j]
        
        return ret
