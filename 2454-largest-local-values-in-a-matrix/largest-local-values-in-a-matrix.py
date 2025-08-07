class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # go in advance of three, checking the values 
        # then iterate through the sub-matrix and find the maximum
        ret = []
        n = len(grid)
        for _ in range(n - 2):
            ret.append([0] * (n - 2))
        count = 0

        for ROW in range(n - 2):
            for COL in range(n - 2):
                # each ROW, COL pair should represent the top left corner of my subgrid
                maxValue = 0
                for i in range(ROW, ROW + 3):
                    for j in range(COL, COL + 3):
                        maxValue = max(maxValue, grid[i][j])
                ret[ROW][COL] = maxValue
                count += 1
        
        return ret




        