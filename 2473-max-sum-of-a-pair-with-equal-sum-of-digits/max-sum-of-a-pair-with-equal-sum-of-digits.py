class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # have a map that marks the sum of digits with the index of the number
        # that is largest. then whenever you encounter a number with that amount of
        # digits, you compare and then set accordingly.

        def sum_digits(num):
            copy = num
            ret = 0

            while copy > 0:
                ret += copy % 10
                copy //= 10
            
            return ret

        m = defaultdict(int)
        s = 0
        res = float('-inf')

        for i in range(len(nums)):
            sum_digit = sum_digits(nums[i])
            if sum_digit in m:
                res = max(res, nums[i] + nums[m[sum_digit]])
            if sum_digit not in m or nums[i] > nums[m[sum_digit]]:
                m[sum_digit] = i
        
        return res if res > float('-inf') else -1