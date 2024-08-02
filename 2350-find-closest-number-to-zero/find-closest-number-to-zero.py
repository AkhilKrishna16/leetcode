class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_dist = float('inf')
        num = 0
        for i in nums:
            if min_dist > abs(i):
                min_dist = abs(i)
                num = i
              
            elif min_dist == abs(i):
                num = max(i, num)
               
        
        return num