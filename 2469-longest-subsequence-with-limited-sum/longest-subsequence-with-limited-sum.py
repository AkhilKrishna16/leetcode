class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # use a prefix sum
        # and for each of the queries
        # utilize a binary search on prefix_sum array of nums
        # and make it so that you are recording the 
        nums.sort()
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        res = [0] * len(queries)
        for i in range(len(queries)):
            low, high = 0, len(prefix) - 1
            while low <= high:
                mid = (low + high) // 2
                if prefix[mid] <= queries[i]:
                    low = mid + 1
                else:
                    high = mid - 1
            res[i] = low
        
        return res
                 
