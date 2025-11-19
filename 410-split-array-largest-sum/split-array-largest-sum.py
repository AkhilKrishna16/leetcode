class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        def check(minimum_sum_allowed):
            required_splits = 0
            curr_sum = 0

            for n in nums:
                if curr_sum + n > minimum_sum_allowed:
                    required_splits += 1
                    curr_sum = n
                else:
                    curr_sum += n
            
            return required_splits + 1 <= k

        while left < right:
            minimum_sum_per_subarray = (left + right) // 2
            if check(minimum_sum_per_subarray):
                right = minimum_sum_per_subarray
            else:
                left = minimum_sum_per_subarray + 1
        return left