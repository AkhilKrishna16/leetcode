class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # traverse based on directions, if right -> switch to down, etc.
        # switch directions based on indices and where overflow is

        UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
        ans = []
        i = 0
        j = 0
        RIGHT_WALL = len(matrix[0]) - 1
        LEFT_WALL = 0
        UP_WALL = 1
        DOWN_WALL = len(matrix) - 1
        direction = RIGHT

        while len(ans) != len(matrix) * len(matrix[0]):
            if direction == RIGHT:
                while j <= RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j += 1
                
                j -= 1
                i += 1
                direction = DOWN
                RIGHT_WALL -= 1
            elif direction == LEFT:
                while j >= LEFT_WALL:
                    ans.append(matrix[i][j])
                    j -= 1
                
                j += 1
                i -= 1
                direction = UP
                LEFT_WALL += 1
            elif direction == UP:
                while i >= UP_WALL:
                    ans.append(matrix[i][j])
                    i -= 1
                
                UP_WALL += 1
                direction = RIGHT
                i += 1
                j += 1
            elif direction == DOWN:
                while i <= DOWN_WALL:
                    ans.append(matrix[i][j])
                    i += 1
                DOWN_WALL -= 1
                direction = LEFT
                i -= 1
                j -= 1
        return ans
