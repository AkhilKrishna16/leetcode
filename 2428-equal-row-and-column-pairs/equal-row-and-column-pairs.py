class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m = defaultdict(int)
        ret = 0

        for i in range(len(grid)): # mark every thing for the rows
            m[tuple(grid[i])] += 1

        for i in range(len(grid)):
            curr = []
            for j in range(len(grid)):
                curr.append(grid[j][i])
            curr = tuple(curr)
            ret += m[curr]
        
        return ret


