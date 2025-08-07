class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(ROW, COL, currString, visited):
            if currString == word:
                return True
            if ROW < 0 or ROW >= len(board) or COL < 0 or COL >= len(board[0]) or len(currString) >= len(word) or visited[ROW][COL] or board[ROW][COL] != word[len(currString)]:
                return False
            newString = currString + board[ROW][COL]
            visited[ROW][COL] = True
            res =  dfs(ROW + 1, COL, newString, visited) or dfs(ROW, COL + 1, newString, visited) or dfs(ROW - 1, COL, newString, visited) or dfs(ROW, COL - 1, newString, visited)

            visited[ROW][COL] = False
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = []
                for _ in range(len(board)):
                    visited.append([False] * len(board[0]))
                if dfs(i, j, "", visited):
                    return True
        
        return False
        
        