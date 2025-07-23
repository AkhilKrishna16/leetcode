class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        i = 0
        ret = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            end = len(nums) - 1
            start = i + 1
            while start < end:
                s = nums[i] + nums[end] + nums[start]

                if s == 0:
                    ret.append([nums[i], nums[end], nums[start]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]: start += 1
                    while start < end and nums[end] == nums[end + 1]: end -= 1
                elif s < 0:
                    start += 1
                else:
                    end -= 1

        return ret
        
