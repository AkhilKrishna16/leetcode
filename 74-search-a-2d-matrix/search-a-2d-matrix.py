class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we first have to find the row
        # and then perform regular binary search within that index

        # 1, 2
        low, high = 0, (len(matrix[0]) * len(matrix)) - 1
        while low <= high:
            mid = (low + high) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            curr = matrix[row][col]

            if curr == target:
                return True
            
            if curr < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False