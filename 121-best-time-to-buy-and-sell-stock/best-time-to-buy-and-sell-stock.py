class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) solution: 
        max_prof = 0 # 7
        min_val = float('inf')

        for price in prices:
            min_val = min(min_val, price) # 1
            max_prof = max(max_prof, price - min_val) # 3  
        
        return max_prof
