class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def is_valid(i, j):
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])
        # start off from (0, 0) with k obstacles left and 0 steps taken
        seen = {(0, 0, k)}
        q = deque([(0, 0, k, 0)])
        ret = float('inf')
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        while q:
            n = len(q)
            for _ in range(n):
                el = q.popleft()
                if el[0] == len(grid) - 1 and el[1] == len(grid[0]) - 1:
                    return el[3]
                for dx, dy in directions:
                    new_row = dx + el[0]
                    new_col = dy + el[1]
                    if is_valid(new_row, new_col) and el[2] - grid[new_row][new_col] >= 0 and (new_row, new_col, el[2] - grid[new_row][new_col]) not in seen:
                        seen.add((new_row, new_col, el[2] - grid[new_row][new_col]))
                        q.append((new_row, new_col, el[2] - grid[new_row][new_col], el[3] + 1))
        return -1


