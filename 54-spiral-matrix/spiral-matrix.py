class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # start off going to the right
        # whenever we hit an out of bounds, switch the direction -- this affects what indices are
        # affected (for instance, if DIR == 2 (DOWN), then we go -1)
        # the only problem is the top going to right -- we have to stop it before it goes to 1, not zero
        # whenever we run into a bounds OR an index pair that already exists, change the direction
        # whenever the length of the list is == the number of elements, break

        DIR = 0
        curr_index = 0
        ROW, COL = 0, 0
        indexes = []
        ret = []

        while len(indexes) != len(matrix) * len(matrix[0]):
            if DIR == 0:
                indexes.append((ROW, COL))
                
                if COL + 1 >= len(matrix[0]) or (ROW, COL + 1) in indexes:
                    DIR += 1
                    DIR %= 4
                    ROW += 1
                else:
                    COL += 1
            elif DIR == 1:
                indexes.append((ROW, COL))
                
                if ROW + 1 >= len(matrix) or (ROW + 1, COL) in indexes:
                    DIR += 1
                    DIR %= 4
                    COL -= 1
                else:
                    ROW += 1
            elif DIR == 2:
                indexes.append((ROW, COL))
                
                if COL - 1 < 0 or (ROW, COL - 1) in indexes:
                    DIR += 1
                    DIR %= 4
                    ROW -= 1
                else:
                    COL -= 1
            elif DIR == 3:
                indexes.append((ROW, COL))
                
                if ROW - 1 < 0 or (ROW - 1, COL) in indexes:
                    DIR += 1
                    DIR %= 4
                    COL += 1
                else:
                    ROW -= 1
            
        for index in indexes:
            ret.append(matrix[index[0]][index[1]])
        
        return ret