class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # you could run from every 0, every cell, or every 1
        # 

        def is_valid(i, j):
            return i >= 0 and i < len(mat) and j >= 0 and j < len(mat[0]) and mat[i][j] == 1
        q = deque([])
        seen = set()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    seen.add((i, j))
        
        ret = [[float('inf')] * len(mat[0]) for _ in range(len(mat))]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            n = len(q)
            for _ in range(n):
                row, col, steps = q.popleft()
                ret[row][col] = min(steps, ret[row][col])

                for dx, dy in directions:
                    new_row = dx + row
                    new_col = dy + col

                    if (new_row, new_col) not in seen and is_valid(new_row, new_col):
                        q.append((new_row, new_col, steps + 1))
                        seen.add((new_row, new_col))
        
        return ret
