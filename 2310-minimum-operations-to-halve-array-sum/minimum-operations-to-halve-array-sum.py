class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # use a max heap and pop off elements to half and add them back
        # go while the value of the sum of the nums is greater than half 
        half = sum(nums) / 2
        nums = [-num for num in nums]
        heapq.heapify(nums)
        ops = 0
        while half > 0:
            max_el = (-heapq.heappop(nums)) / 2
            half -= max_el
            heapq.heappush(nums, -max_el)
            ops += 1
        
        return ops
        

