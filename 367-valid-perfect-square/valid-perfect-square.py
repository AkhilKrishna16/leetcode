class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num

        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid < num:
                start = mid + 1
            elif mid * mid > num:
                end = mid - 1
            else:
                return True
        
        return False