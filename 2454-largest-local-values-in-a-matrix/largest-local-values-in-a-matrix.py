class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # go in advance of three, checking the values 
        # then iterate through the sub-matrix and find the maximum
        ret = []
        n = len(grid) - 2
        for _ in range(n):
            ret.append([-1] * n)
        
        for R in range(n):
            for C in range(n):
                maxValue = float('-inf')
                for i in range(R, R + 3):
                    for j in range(C, C + 3):
                        maxValue = max(maxValue, grid[i][j])
                ret[R][C] = maxValue
        
        return ret





        