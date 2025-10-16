class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def is_valid(i, j):
            return i >= 0 and j >= 0 and i < len(mat) and j < len(mat[0]) and mat[i][j] == 1 and (i, j) not in seen
        # add to the queue the cells with a 0
        q = deque([])
        seen = set()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    seen.add((i, j))
        
        # go through the queue and add to ret

        # form ret
        ret = []
        for _ in range(len(mat)):
            ret.append([-1] * len(mat[0]))
        
        # go through the queue and mark
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            n = len(q)
            for _ in range(n):
                el = q.popleft()
                ret[el[0]][el[1]] = el[2] # mark the current

                # append the new elements
                for dx, dy in directions:
                    new_row = el[0] + dx
                    new_col = el[1] + dy
                    if is_valid(new_row, new_col):
                        seen.add((new_row, new_col))
                        q.append((new_row, new_col, el[2] + 1))
        return ret


                
