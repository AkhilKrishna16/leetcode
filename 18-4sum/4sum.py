class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ret = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    s = nums[start] + nums[i] + nums[j] + nums[end]
                    if s == target:
                        ret.append([nums[start], nums[i], nums[j], nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start - 1]: start += 1
                        while start < end and nums[end] == nums[end + 1]: end -= 1
                    elif s < target:
                        start += 1
                    else: 
                        end -= 1
        
        return ret