class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # essentially, if the count that has been processed, the number of fresh -> turned to rotten + empty is m x n, ur done.
        # find all rotten ones. add to queue. 
        # then you go through minute by minute
        # 

        q = deque([])
        ret = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        
        while q:
            row, col, minutes = q.popleft()
            ret = minutes

            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    q.append((new_row, new_col, minutes + 1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return ret
            