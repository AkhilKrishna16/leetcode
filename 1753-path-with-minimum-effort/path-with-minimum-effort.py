class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def is_valid(i, j):
            return i >= 0 and i < len(heights) and j >= 0 and j < len(heights[0])
        
        def check(min_effort): # check all paths
            seen = {(0, 0)}
            stack = [(0, 0)]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while stack:
                x, y = stack.pop()
                if (x, y) == (len(heights) - 1, len(heights[0]) - 1):
                    return True
                
                for dx, dy in directions:
                    next_row, next_col = dx + x, dy + y
                    if is_valid(next_row, next_col) and (next_row, next_col) not in seen:
                        if abs(heights[next_row][next_col] - heights[x][y]) <= min_effort:
                            stack.append((next_row, next_col))
                            seen.add((next_row, next_col))
                
            return False
        
        left, right = 0, max(max(row) for row in heights)
        while left <= right:
            min_effort = (left + right) // 2
            if check(min_effort):
                right = min_effort - 1
            else:
                left = min_effort + 1

        return left 
