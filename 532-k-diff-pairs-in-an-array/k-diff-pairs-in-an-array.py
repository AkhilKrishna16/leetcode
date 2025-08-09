class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # sort by absolute value to match the smallest elements first
        # then skip all duplicates to avoid matching those since we already have them
        # [1, 1, 3, 4, 5] -> (1, 3), (3, 5)

        nums = sorted(nums)
        count = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            while j < len(nums) and abs(nums[j] - nums[i]) < k:
                j += 1
            print(j)
            if j < len(nums) and abs(nums[j] - nums[i]) == k:
                print(nums[j], nums[i])
                count += 1
        
        return count
            
