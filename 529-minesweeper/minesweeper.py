class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # if we click on M, then we change to X and just return right?
        # if we click on an E, then we iterate through the outside, only if there are no mines 
        # this means that if it ends up being a B, then we can dfs in all 8 directions
        # if click on a number, then we can't necessarily iterate through out because that ruins the game 
        # so we are stuck
        directions = [(1,0), (0,1), (-1,0), (0,-1), (-1,-1), (1,1), (-1,1), (1,-1)]
        def dfs(i, j):
            # check all 8 neighbors and update count
            count = 0
            for dx, dy in directions:
                new_row = dx + i
                new_col = dy + j

                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == 'M':
                    count += 1
            
            if count > 0:
                board[i][j] = str(count)
                return
            
            board[i][j] = 'B'
            # in this case, we can iterate and dfs on all possible edges
            for dx, dy in directions:
                new_row = dx + i
                new_col = dy + j

                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == 'E':
                    dfs(new_row, new_col)



        click_x, click_y = click

        if board[click_x][click_y] == 'M':
            board[click_x][click_y] = 'X'
            return board
        elif board[click_x][click_y] == 'E':
            # then you have to check all adjacent boxes for mines
            # and then either replace with number of mines around or 'B'
            dfs(click_x, click_y)
        
        return board

