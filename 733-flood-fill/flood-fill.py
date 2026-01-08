class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # dfs from the starting cell
        # mark everything as the color
        # only if the cell is the same as image[sr][sc]
        
        source = image[sr][sc]
        
        q = deque([(sr, sc)])
        seen = {(sr, sc)}
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            r, c = q.pop()
            image[r][c] = color

            for dx, dy in directions:
                new_row = r + dx
                new_col = c + dy
                if new_row >= 0 and new_row < len(image) and new_col >= 0 and new_col < len(image[0]) and image[new_row][new_col] == source and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    q.append((new_row, new_col))
        
        return image

