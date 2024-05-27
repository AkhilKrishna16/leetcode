class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) solution: 
        max_prof = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)
            max_prof = max(price - min_price, max_prof)
        
        return max_prof
