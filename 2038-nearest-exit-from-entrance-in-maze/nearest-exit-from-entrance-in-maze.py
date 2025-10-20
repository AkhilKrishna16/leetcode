class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque([(entrance[0], entrance[1], 0)])
        seen = {(entrance[0], entrance[1])}

        def is_valid(row, col):
            return row >= 0 and col >= 0 and row < len(maze) and col < len(maze[0]) and maze[row][col] == '.'
        
        def is_at_edge(row, col):
            return row == 0 or col == 0 or row == len(maze) - 1 or col == len(maze[0]) - 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            recent = q.popleft()
            if is_at_edge(recent[0], recent[1]) and (recent[0], recent[1]) != tuple(entrance):
                return recent[2]
            for dx, dy in directions:
                new_row = dx + recent[0]
                new_col = dy + recent[1]
                if is_valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    q.append((new_row, new_col, recent[2] + 1))
        
        return -1
