class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        [1, 8, 11, 17, 22, 28], left = prefix[i - 1], right = prefix[-1] - prefix[i]
        """
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        for i in range(len(nums)):
            left = 0 if i == 0 else prefix[i - 1]
            right = prefix[-1] - prefix[i]
            if left == right:
                return i
        
        return -1
