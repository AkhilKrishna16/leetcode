class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # have a prefix sum array
        # keep track of a left sum and a right sum
        # mark the current point and have a o(n) one pass solution such that 
        # it goes through each marker up till n - 2 and increment count if 
        # left >= right

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        count = 0
        for i in range(0, len(nums) - 1):
            if prefix[-1] - prefix[i] <= prefix[i]:
                count += 1
        
        return count