class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we can use a bfs solution with steps to identify how long it would take to get rid of all oranges at a certain minute
        # we have to wait for all fresh oranges to become rotten or there are no fresh oranges
        # first append all the rotten oranges to queue (and the seen set)
        # we have to count the number of oranges
        # in this case, clear out all the oranges through the bfs
        # then at the end, perform O(n^2) check and just check if there are any leftover oranges

        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        def is_valid(i, j):
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == FRESH
        
        q = deque([])
        seen = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == ROTTEN: # rotten
                    q.append((i, j, 0))
                    seen.add((i, j))
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        ret = 0
        while q:
            row, col, steps = q.popleft()
            # turn this into a rotten orange
            grid[row][col] = ROTTEN
            ret = steps
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy

                if is_valid(new_row, new_col) and (new_row, new_col) not in seen:
                    q.append((new_row, new_col, steps + 1))
                    seen.add((new_row, new_col))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == FRESH:
                    return -1
        return ret
        
            

